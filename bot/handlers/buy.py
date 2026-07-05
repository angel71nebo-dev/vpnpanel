from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "🛒 Купить VPN")
async def buy_vpn(message: Message):
    await message.answer(
        "🛒 Купить VPN\n\n"
        "Раздел находится в разработке."
    )
