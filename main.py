## main.py
from aiogram.types import InputTextMessageContent, Message
from aiogram.client.bot import DefaultBotProperties
from aiogram import Bot, Dispatcher, Router, F
from dotenv import load_dotenv
import asyncio
import logging
import os

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
router = Router()
####*

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("notes_spirit_bot")

####*
dp.include_router(router)
async def main():
    print("ЕЕЕ, ЗАПУСТИВСЯ!!")
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

