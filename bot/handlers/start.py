from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from db import db

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):

    username = message.from_user.username or ""

    user = db.get_user(message.from_user.id)

    if user is None:
        db.add_user(
            telegram_id=message.from_user.id,
            username=username,
        )

        text = (
            "👋 Добро пожаловать в VPNPanel!\n\n"
            "Вы успешно зарегистрированы."
        )

    else:
        db.update_username(
            telegram_id=message.from_user.id,
            username=username,
        )

        text = (
            "👋 С возвращением!\n\n"
            "VPNPanel готова к работе."
        )

    await message.answer(text)
