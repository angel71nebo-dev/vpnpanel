from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "🔑 Мои VPN")
async def my_vpn(message: Message):

    await message.answer(
        "🔑 Ваши VPN\n\n"
        "У вас пока нет созданных VPN."
    )
