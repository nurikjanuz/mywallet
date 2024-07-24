from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton("/start")).insert(KeyboardButton("/help"))
    btn.add(KeyboardButton("/income")).insert(KeyboardButton("/expenses"))
    btn.add(KeyboardButton("/operations_history")).insert(KeyboardButton("/report"))
    btn.add(KeyboardButton("/currency"))
    return btn
