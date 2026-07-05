from aiogram.utils.keyboard import InlineKeyboardBuilder


def servers_keyboard(days: int):
    kb = InlineKeyboardBuilder()

    kb.button(
        text="🇬🇧 Англия (006)",
        callback_data=f"server_006_{days}"
    )

    kb.button(
        text="🇫🇮 Финляндия (145)",
        callback_data=f"server_145_{days}"
    )

    kb.adjust(1)

    return kb.as_markup()
