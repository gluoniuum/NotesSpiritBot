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
    print(data)

    desc_rep = {
            'hatha_cb': txts.kibalion_desc,
            'atmos_cb': 'three',
            'magnet_cb': 'four',
            'medium_cb': 'five',
            'forma_cb': 'five',
            'chakra_cb': 'five'}
    for desc in desc_rep:
        await callback.message.answer({desc_rep[desc])
    
#
####
