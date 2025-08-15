## presentation/free_books_choose
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
@rt.callback_query()
async def free_books(callback : CallbackQuery):
    logger.info(f'{callback.message.chat.id}') 
     
   #
####
