## main.py

#### DICT: imp = imports

## long_imp
from aiogram.types import InputTextMessageContent, Message
from aiogram.client.bot import DefaultBotProperties
from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from dotenv import load_dotenv

## short_imp
import asyncio
import logging
import os

## routers_imp
from handlers_command.start import rt as start_router
from handlers_command.free_books import rt as free_router
## Token 
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

## log
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("notes_spirit_bot")


#### main
async def main():
    print(API_TOKEN)
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    log.info("Bot is starting...")

### <routers
    dp.include_router(start_router)
    dp.include_router(free_router)

### >


## awaits
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

#### run
if __name__ == '__main__':
    asyncio.run(main())

