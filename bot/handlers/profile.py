from aiogram import Router, F
from aiogram.types import Message

from db import db

router = Router()


@router.message(F.text == "👤 Профиль")
async def profile(message: Message):

    user = db.get_user(message.from_user.id)

    if user is None:
        await message.answer(
            "Пользователь не найден.\n"
            "Отправьте команду /start."
        )
        return

    await message.answer(
        f"👤 Ваш профиль\n\n"
        f"🆔 Telegram ID: {user['telegram_id']}\n"
        f"👤 Username: @{user['username'] if user['username'] else '-'}\n"
        f"📅 Регистрация: {user['created_at']}\n"
        f"📌 Статус: {user['status']}"
    )
