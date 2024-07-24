from loader import dp, bot, ADMIN
from aiogram import types
from keyboards.inline import voice_ibtn
from keyboards.default import start_btn, start_btn_admin
from utils.database import users, operations
from states import IncomeStates, ExpensesStates
import requests
from aiogram.dispatcher import FSMContext
from filters import IsDigit
HELP_TEXT = f"""
/start - botni ishga tushirish
/help - yordam berish
/income - daromadlarni kiritish
/expenses - xarajatlarni kiritish
/operations_history - barcha operatsiyalar tarixi chiqarishingiz mumkin
/report - umumiy daromad, xarajat va pul qoldiqlarini ko'rishingiz mumkin
/currency - bugunhi Markaziy bank valyuta kursi bilan tanishishingiz mumkin
"""

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id==int(ADMIN):
        await message.answer("Assalomu alaykum ADMIN!", reply_markup=await start_btn_admin())
    else:
        user= users.get_user(user_id)

        if not user:
            users.create_user(user_id, message.from_user.full_name)
        await message.answer(f"Assalomu alaykum. Botimizga xush kelibsiz!\n"
                             f"Ushbu botda daromad va xarajatlaringizni bir valyutada yuritishingiz mumkin!",
                             reply_markup=await start_btn())


@dp.message_handler(commands=["income"])
async def income(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(operation_type="income")
    await message.answer("Daromad izohini kiriting: ")
    await IncomeStates.request_comment.set()

@dp.message_handler(state=IncomeStates.request_comment)
async def request_comment(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(operation_comment=message.text)
    await message.answer("Daromad summasini kiriting: ")
    await IncomeStates.request_sum.set()

@dp.message_handler(IsDigit(), state=IncomeStates.request_sum)
async def request_sum(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(operation_sum=message.text)
    operation_text=await state.get_data()
    print(operation_text)
    operation_type=operation_text['operation_type']
    operation_comment=operation_text['operation_comment']
    operation_sum=operation_text['operation_sum']
    operations.create_operation(user_id, operation_type, operation_comment, operation_sum)
    await message.answer(f"{operation_type}:\n{operation_comment}\n{operation_sum}")
    await state.finish()

@dp.message_handler(commands=["expenses"])
async def expenses(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(operation_type="expenses")
    await message.answer("Xarajat izohini kiriting: ")
    await ExpensesStates.request_comment.set()

@dp.message_handler(state=ExpensesStates.request_comment)
async def request_comment(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(operation_comment=message.text)
    await message.answer("Xarajat summasini kiriting: ")
    await ExpensesStates.request_sum.set()

@dp.message_handler(IsDigit(), state=ExpensesStates.request_sum)
async def request_sum(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(operation_sum=message.text)
    operation_text=await state.get_data()

    operation_type=operation_text['operation_type']
    operation_comment=operation_text['operation_comment']
    operation_sum=operation_text['operation_sum']
    operations.create_operation(user_id, operation_type, operation_comment, operation_sum)
    await message.answer(f"{operation_type}:\n{operation_comment}\n{operation_sum}")
    await state.finish()

@dp.message_handler(commands=["operations_history"])
async def operations_history(message: types.Message):
    user=message.from_user.id
    history = operations.get_operations(user)
    print(history)
    for item in history:
        users_text= f"operation type - {item[2]}\noperation comment - {item[3]}\noperation sum - {item[4]}"
        await message.answer(users_text, parse_mode="HTML")

@dp.message_handler(commands=["report"])
async def report(message: types.Message):
    user=message.from_user.id
    history = operations.get_operations(user)
    total_income = 0
    total_expenses = 0
    for item in history:
        if item[2] == "income":
            total_income+= int(item[4])
        elif item[2] == "expenses":
            total_expenses+= int(item[4])

    users_text= (f"total income = {total_income}\ntotal expenses = {total_expenses}\n"
                 f"left amount of money = {total_income-total_expenses}")
    await message.answer(users_text, parse_mode="HTML")

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(HELP_TEXT, reply_markup=await start_btn())

#pip install requests
@dp.message_handler(commands=["currency"])
async def currency(message: types.Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    data=response.json()
    for item in data:
        if item['Ccy']=="USD" or item["Ccy"]=="EUR" or item['Ccy']=="RUB":
            valyuta=item['Ccy']
            nomi=item['CcyNm_UZ']
            rate=item['Rate']
            date=item['Date']

            text = (f"<b>{nomi}</b>\n"
                    f"<b>1{valyuta}</b> - {rate} so'm\n"
                    f"<b>Sana</b> {date}")
            await message.answer(text, parse_mode='HTML')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
