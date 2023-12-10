import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv, find_dotenv

from callbacks import get_text, get_command
from handlers import start_bot, message_bot, help_bot

load_dotenv(find_dotenv())


async def main():
   
    bot = Bot(
        os.getenv("TOKEN"),
        parse_mode=ParseMode.HTML,
    )
    dp = Dispatcher()
    dp.include_routers(
        start_bot.router,
        help_bot.router,
        message_bot.router,
        get_command.router,
        get_text.router,  
    )
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())