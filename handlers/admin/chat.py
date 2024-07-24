from aiogram import types
from utils.database import users
from loader import dp, bot
from states import MyAdminStates
from filters.admin import IsAdmin
from aiogram.dispatcher import FSMContext

@dp.message_handler(IsAdmin(), commands=["users"])
async def users_command(message: types.Message):
    user = users.get_users_all()
    for item in user:
        users_text= f"user - {item[0]}\nfio - {item[2]}\nphone - {item[3]}"
        await message.answer(users_text, parse_mode="HTML")
        if item[4] and item[5]:
            await bot.send_location(item[1], longitude=item[4], latitude=[5])

@dp.message_handler(IsAdmin(),commands=["post"])
async def users_command_post(message: types.Message):
    await message.answer("Xabarni kiriting: ")
    await MyAdminStates.request_message.set()

@dp.message_handler(IsAdmin(), state=MyAdminStates.request_message)
async def users_command_message(message: types.Message, state: FSMContext):
    mess= message.text
    user = users.get_users_all()
    for item in user:
        await bot.send_message(chat_id=item[1], text=mess, parse_mode="HTML")

    await state.finish()