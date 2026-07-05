import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from db import db
from bot.handlers.start import router as start_router
from bot.handlers.profile import router as profile_router
from bot.handlers.myvpn import router as myvpn_router
from bot.handlers.buy import router as buy_router
from bot.handlers.support import router as support_router
async def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN не указан в файле .env"
        )

    # Инициализация базы
    

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(profile_router)
    dp.include_router(myvpn_router)
    dp.include_router(buy_router)
    dp.include_router(support_router)
    print("===================================")
    print("VPNPanel v2")
    print("База данных подключена")
    print("Бот запускается...")
    print("===================================")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
