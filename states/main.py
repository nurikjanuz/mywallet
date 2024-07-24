from aiogram.dispatcher.filters.state import State, StatesGroup

class MyStates(StatesGroup):
    request_name = State()
    request_phone = State()
    request_age = State()
    request_about = State()


class MyAdminStates(StatesGroup):
    request_message = State()

class IncomeStates(StatesGroup):
    request_type= State()
    request_comment = State()
    request_sum = State()

class ExpensesStates(StatesGroup):
    request_type= State()
    request_comment = State()
    request_sum = State()
