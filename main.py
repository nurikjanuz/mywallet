from aiogram import Bot, Dispatcher, executor
from loader import dp
import handlers
import filters


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
