from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_to_is_sub = InlineKeyboardMarkup()
back_button = InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_is_sub")
back_to_is_sub.row(back_button)


back_to_product = InlineKeyboardMarkup()
back_button = InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_product")
back_to_product.row(back_button)
