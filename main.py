import asyncio
import logging

from aiogram import Bot, Dispatcher
from loguru import logger


import config
import handlers
from db.utils.common import global_init




async def begin_polling():
    bot: Bot = Bot(token=config.BOT_TOKEN)
    dp: Dispatcher = Dispatcher()

    dp.include_router(handlers.main_router)

    logger.info("Begin polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def main():

    logger.info("MAIN")
    await global_init("sqlite+aiosqlite:///./DB.db")
    await begin_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
