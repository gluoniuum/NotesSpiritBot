## presentation/free_books
#
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.types import InputTextMessageContent, Message
from aiogram import Bot, Dispatcher, Router, F
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
@rt.callback_query(F.data == 'free_books_cb')
async def free_books(callback : CallbackQuery):
    logger.info(f'{callback.message.chat.id}') 
    await callback.answer('')
    await callback.message.answer('Вот Наша Библиотека Бесплатных Книг', reply_markup = kb.free_menu) 
   #
####
