import asyncio

from aiogram import Bot, Dispatcher

from app.database.models import async_main

from app.user import user
from app.admin import admin

from config import API_TOKEN

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_routers(user, admin)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

async def on_startup():
    await async_main()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass