from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loader import ADMIN


class IsAdmin(BoundFilter):
    async def check(self, message: Message) -> bool:
        if message.from_user.id==int(ADMIN):
            return True
        else:
            return False

class IsAlpha(BoundFilter):
    async def check(self, message: Message) -> bool:
        if message.text.isalpha():
            return True
        else:
            await message.answer("Harflardan iborat tekst kiriting! ")

class IsDigit(BoundFilter):
    async def check(self, message: Message) -> bool:
        if message.text.isdigit():
            return True
        else:
            await message.answer("Sonlardan iborat tekst kiriting! ")