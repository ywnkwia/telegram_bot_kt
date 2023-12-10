from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils import markdown 
from keyboards import reply,inline

router = Router()



@router.message()
async def command_start(message:Message):
    msg = message.text.lower()
    if msg == "читать гороскоп":
        await message.answer("Выберете свой знак зодиака:",reply_markup=inline.goroskop_keyboard)     
         
    elif msg == "назад":
        await message.answer("Выберете,какое аниме будете смотреть сегодня:",reply_markup=reply.start) 
        
    else :
        await message.reply("Я не понимаю вас, введите одну из команд! \n /start")
        
async def get_goroskop(callback: CallbackQuery):
    await callback.answer()
    zodiac = callback.data