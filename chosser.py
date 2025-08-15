# chosser
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
import repositories.free_books as rep
import modules.texts as txts
#
## repository
rt = Router()
logger = logging.getLogger(__name__)
#
@rt.callback_query()
async def chosser_books(callback : CallbackQuery):
    logger.info(f'{callback.message.chat.id}')
    data = callback.data
    
    for desc in rep.desc_rep:
        if data == desc: 
            await callback.answer('') 
            await callback.message.answer(rep.desc_rep[desc])
    
#
####
