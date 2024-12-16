from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb
from app.database.requests import set_user

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer('Привет', reply_markup=kb.main)