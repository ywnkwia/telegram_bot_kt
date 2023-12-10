from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils import markdown 
from keyboards import reply,inline

router = Router()

@router.message(Command("help"))
async def command_start(message:Message):
    #url = "https://sakhalife.ru/wp-content/uploads/2023/07/numerology-collage-concept.jpg" 
    text = markdown.text(
        #markdown.hide_link(url),
        f"Привет,{markdown.hbold(message.from_user.full_name)},держи команды нашего бота! \n \n Выберете и нажмите на нужную вам команду \n /start - Старт \n /horoscope - Показать гороскоп на сегодня \n /review - Написать отзыв \n /back - Вернуться в самое начало :",
    )
    await message.reply(
        text=text,
    )