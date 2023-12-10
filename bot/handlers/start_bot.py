from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils import markdown 
from keyboards import reply,inline

router = Router()

@router.message(CommandStart())
async def command_start(message:Message):
    url = "https://sakhalife.ru/wp-content/uploads/2023/07/numerology-collage-concept.jpg" 
    text = markdown.text(
        markdown.hide_link(url),
        f"Привет,{markdown.hbold(message.from_user.full_name)},мы очень рады ,что вы пользуетесь нашим телеграмм ботом! \n \n Выберете ,чем хотите заняться:",
    )
    await message.reply(
        text=text,
        reply_markup=inline.start_keyboard
    )
