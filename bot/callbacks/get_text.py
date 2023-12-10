from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import requests
from bs4 import BeautifulSoup 
from keyboards import inline,reply
from aiogram.utils import markdown
from aiogram.enums import ChatAction

router = Router()
   
@router.callback_query(F.data == "aries")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/aries/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')

    url_photo = "https://cdn.nur.kz/images/1120x630/8c4ddcb1c8f3012c.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n",
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "taurus")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/taurus/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/7b341e728b289b86.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,  
    )
    
@router.callback_query(F.data == "gemini")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/gemini/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.7days.ru/pic/b82/981127/1439718/86.jpg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "cancer")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/cancer/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/a72829b250a1b561.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "leo")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/leo/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/439eda5c06e92043.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "virgo")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/virgo/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/bb187cfc6ea9c637.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )
    
@router.callback_query(F.data == "libra")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/libra/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/9c29663417c3afac.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "scorpio")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/scorpio/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/3a63e5d37296ff9c.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "sagittarius")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/sagittarius/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/39b48af3c5d040d9.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "capricorn")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/capricorn/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/0c4e5da92b882d18.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "aquarius")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/aquarius/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/fe689eb2f629fed2.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

@router.callback_query(F.data == "pisces")
async def aries(callback: CallbackQuery):
    url = "https://horo.mail.ru/prediction/pisces/today/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'article__item article__item_alignment_left article__item_html')
    
    url_photo = "https://cdn.nur.kz/images/1120x630/8c4ddcb1c8f3012c.jpeg"
    text = markdown.text(
        markdown.hide_link(url_photo),
        f"Вот ваш гороскоп на сегодня: \n \n {temp.text}",
        sep = "\n"
    )
    await callback.message.answer(
        text=text,
        action=ChatAction.TYPING,
        reply_markup=inline.zodiac_keyboard,
    )

