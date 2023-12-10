from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards import inline,reply
from aiogram.enums import ChatAction
from aiogram.utils import markdown

router = Router()

@router.callback_query(F.data == "read_goroskop")
async def aries(callback: CallbackQuery):
    url = "https://sakhalife.ru/wp-content/uploads/2023/07/numerology-collage-concept.jpg" 
    text = markdown.text(
        markdown.hide_link(url),
        f"Выбирите ваш знак зодиака:",
    )
    await callback.message.answer(
        text=text,
        reply_markup=inline.goroskop_keyboard,
        action = ChatAction.TYPING,
    )
    
@router.callback_query(F.data == "back")
async def aries(callback: CallbackQuery):
    url = "https://sakhalife.ru/wp-content/uploads/2023/07/numerology-collage-concept.jpg" 
    text = markdown.text(
        markdown.hide_link(url),
        f"Выберете ,чем хотите заняться:",
    )
    await callback.message.answer(
        reply_markup=inline.start_keyboard,
        action = ChatAction.TYPING,
    )

@router.callback_query(F.data == "goroskop")
async def aries(callback: CallbackQuery):
    url = "https://sakhalife.ru/wp-content/uploads/2023/07/numerology-collage-concept.jpg" 
    text = markdown.text(
        markdown.hide_link(url),
        f"Выбирите ваш знак зодиака:",
    )
    await callback.message.answer(
        text=text,
        reply_markup=inline.goroskop_keyboard,
        action = ChatAction.TYPING,
    )