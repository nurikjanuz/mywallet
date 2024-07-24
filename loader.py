import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

bot_token = os.getenv("BOT_TOKEN")
ADMIN = os.getenv("ADMIN")

storage = MemoryStorage()
bot = Bot(bot_token)
dp = Dispatcher(bot, storage=storage)

