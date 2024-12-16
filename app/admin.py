from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
from aiogram.fsm.context import FSMContext

admin = Router()


class Admin(Filter):
   async def __call__(self, message: Message):
       return message.from_user.id in [000, 864453930]

@admin.message(Admin(), Command('admin'))
async def cmd_admin(message: Message):
    await message.answer('Вы Админ!')