from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def start_btn_admin():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton("/start")).insert(KeyboardButton("/users"))
    btn.add(KeyboardButton("/post"))
    return btn
