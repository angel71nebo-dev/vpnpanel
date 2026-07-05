from aiogram.utils.keyboard import InlineKeyboardBuilder


def tariffs_keyboard():
    kb = InlineKeyboardBuilder()

    kb.button(text="🟢 7 дней — 99 ₽", callback_data="buy_7")
    kb.button(text="🔵 30 дней — 299 ₽", callback_data="buy_30")
    kb.button(text="🟣 90 дней — 799 ₽", callback_data="buy_90")

    kb.adjust(1)

    return kb.as_markup()
