from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back = InlineKeyboardMarkup()

back_button = InlineKeyboardButton(text="🔙 Назад", callback_data="back_button_no_sub")

back.row(back_button)
