from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "💬 Поддержка")
async def support(message: Message):
    await message.answer(
        "💬 Поддержка\n\n"
        "Если возникли вопросы или проблемы,\n"
        "обратитесь к администратору.\n\n"
        "Контакт: @angel71nebo"
    )
