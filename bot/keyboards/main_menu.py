from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔑 Мои VPN"),
            KeyboardButton(text="🛒 Купить VPN"),
        ],
        [
            KeyboardButton(text="👤 Профиль"),
            KeyboardButton(text="💬 Поддержка"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие...",
)
