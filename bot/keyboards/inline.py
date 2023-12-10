from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

goroskop_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="♈ Овен ♈", callback_data="aries"),
        InlineKeyboardButton(text="♉ Телец ♉", callback_data="taurus"),
        InlineKeyboardButton(text="♊ Близнецы ♊", callback_data="gemini"),
    ],
    [
        InlineKeyboardButton(text="♋ Рак ♋", callback_data="cancer"),
        InlineKeyboardButton(text="♌ Лев ♌", callback_data="leo"),
        InlineKeyboardButton(text="♍ Дева ♍", callback_data="virgo"),
    ],
    [
        InlineKeyboardButton(text="♎ Весы ♎", callback_data="libra"),
        InlineKeyboardButton(text="♏ Скорпион ♏", callback_data="scorpio"),
        InlineKeyboardButton(text="♐ Стрелец ♐", callback_data="sagittarius"),
    ],
    [
        InlineKeyboardButton(text="♑ Козерог ♑", callback_data="capricorn"),
        InlineKeyboardButton(text="♒ Водолей ♒", callback_data="aquarius"),
        InlineKeyboardButton(text="♓ Рыбы ♓", callback_data="pisces"),      
    ],
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="back"),
    ],
],
    resize_keyboard=True, 
    one_time_keyboard=True,  
    selective=True, 
)

zodiac_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⬅️ Назад", callback_data="back"),
        InlineKeyboardButton(text="Еще гороскопы 🌌", callback_data="goroskop"),
    ],
],
    resize_keyboard=True, 
    one_time_keyboard=True,  
    selective=True, 
)

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Читать гороскоп", callback_data="read_goroskop"),
        
    ],
],
    resize_keyboard=True, 
    one_time_keyboard=True,  
    selective=True, 
)