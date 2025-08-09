## presentation/start.py
#
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.types import InputTextMessageContent, Message
from aiogram import Bot, Dispatcher, Router 
from aiogram.filters import Command
#
import aiosqlite
import asyncio 
import logging
#
import modules.keyboards as kb
#

rt = Router()
logger = logging.getLogger(__name__)
#

@rt.message(Command('start'))
async def start(message : Message):
    # 
    name = message.from_user.username ## username
    chat_id = message.chat.id ## chat_id
    #
    logger.info(f'{name} : {chat_id} : {message.text}')
    await message.answer('Приветсвуем в Нашем Книжном Магазине \"Мысли Души\"📓', reply_markup = kb.start_menu)
    #
####
