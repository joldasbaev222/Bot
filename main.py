from aiogram import Bot, Dispatcher
from config import token
import asyncio
from routers import router
from database import init_db   # 👈 import bor

my_bot = Bot(token=str(token))
dp = Dispatcher()


async def main():
    await init_db()            # 👈 MANA SHU QATOR YETISHMAYOTGANDI
    print("I am starting ...")
    dp.include_routers(router)
    await dp.start_polling(my_bot)


if __name__ == "__main__":
    asyncio.run(main())
