import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.db.models import async_main

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')