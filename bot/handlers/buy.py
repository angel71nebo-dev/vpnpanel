from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from bot.keyboards.tariffs import tariffs_keyboard
from bot.keyboards.servers import servers_keyboard
from db import db

router = Router()


@router.message(F.text == "🛒 Купить VPN")
async def buy_vpn(message: Message):

    user = db.get_user(message.from_user.id)

    if user is None:
        await message.answer("Сначала отправьте команду /start")
        return

    await message.answer(
        "🛒 <b>Покупка VPN</b>\n\n"
        "Выберите тариф:",
        reply_markup=tariffs_keyboard()
    )
@router.callback_query(F.data == "buy_7")
async def buy_7(callback: CallbackQuery):
    await callback.message.answer(
        "🟢 Вы выбрали тариф на 7 дней.\n\n"
        "Теперь выберите сервер:",
        reply_markup=servers_keyboard(7)
    )
    await callback.answer()


@router.callback_query(F.data == "buy_30")
async def buy_30(callback: CallbackQuery):
    await callback.message.answer(
        "🔵 Вы выбрали тариф на 30 дней.\n\n"
        "Теперь выберите сервер:",
        reply_markup=servers_keyboard(30)
    )
    await callback.answer()


@router.callback_query(F.data == "buy_90")
async def buy_90(callback: CallbackQuery):
    await callback.message.answer(
        "🟣 Вы выбрали тариф на 90 дней.\n\n"
        "Теперь выберите сервер:",
        reply_markup=servers_keyboard(90)
    )
    await callback.answer()
    
@router.callback_query(F.data.startswith("server_"))
async def select_server(callback: CallbackQuery):
    _, server, days = callback.data.split("_")

    await callback.message.answer(
        f"✅ Вы выбрали:\n\n"
        f"Сервер: {server}\n"
        f"Срок: {days} дней\n\n"
        f"Следующий этап — создание заказа и оплата через ЮMoney."
    )

    await callback.answer()