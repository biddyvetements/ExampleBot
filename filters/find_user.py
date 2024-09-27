from typing import Union

from aiogram.filters import Filter

from db.models import User
from db.utils.user import get_user_by_tg_id
from aiogram.types import Message


class FindUserFilter(Filter):
    async def __call__(
            self,
            message: Message
    ) -> dict:
        user = await get_user_by_tg_id(user_id=message.chat.id)
        return {"user": user} if user else False
