import re

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, and_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters import FindUserFilter
from states import NameFetcher
from db.utils.user import insert_user
from db.models import User
from utils import get_usd_price
from utils.user_utils import unescape_markdown

main_router = Router()


@main_router.message(and_f(CommandStart(), FindUserFilter()))
async def start_handler(message: Message, user: User):
    usd_price = await get_usd_price()
    await message.answer(f'👋 Приветствую, *{unescape_markdown(user.name)}*!\n\n'
                         f'💲 Текущая цена за `1` USD: `{usd_price}` руб.', parse_mode=ParseMode.MARKDOWN)


@main_router.message(CommandStart())
async def begin_fetch_name(message: Message, state: FSMContext):
    await message.answer("Мы еще не знакомы 😕\n"
                         "Отправьте свое имя в следующем сообщении что бы я смог запомнить вас")
    await state.set_state(NameFetcher.name_waiting)


@main_router.message(NameFetcher.name_waiting)
async def end_fetch_name(message: Message, state: FSMContext):
    user = User(id=message.chat.id, name=message.text.strip())
    await insert_user(user)
    await state.clear()
    await message.answer(f'☺️ Рад знакомству, *{unescape_markdown(user.name)}*!', parse_mode=ParseMode.MARKDOWN)

    await start_handler(message, user)
