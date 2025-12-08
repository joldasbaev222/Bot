from aiogram import Bot, Dispatcher
from config import token
import asyncio
from routers import router

my_bot = Bot('8226534324:AAH5PMaaIoqBZTELTMrNZJ77ZMqcX_Lklj8')
dp = Dispatcher()


async def main():
    print("I am starting ...")
    dp.include_routers(router)
    await dp.start_polling(my_bot)


# if __name__ == "__main__": 
    asyncio.run(main())