import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import Database


async def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN не указан в файле .env"
        )

    # Инициализация базы
    Database()

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    print("===================================")
    print("VPNPanel v2")
    print("База данных подключена")
    print("Бот запускается...")
    print("===================================")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
