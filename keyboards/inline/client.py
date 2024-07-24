from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def social_ibtn():
    ibtn = InlineKeyboardMarkup()
    ibtn.add(InlineKeyboardButton("Google", callback_data="google"))
    ibtn.add(InlineKeyboardButton("Youtube", callback_data="youtube"))
    return ibtn

async def voice_ibtn():
    lbtn = InlineKeyboardMarkup()
    lbtn.add(InlineKeyboardButton("like", callback_data="like"))
    lbtn.add(InlineKeyboardButton("dislike", callback_data="dislike"))
    return lbtn