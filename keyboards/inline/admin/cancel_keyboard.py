from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel = InlineKeyboardMarkup()

cancel_button = InlineKeyboardButton(text="Отмена ❌", callback_data="cancel")

cancel.row(cancel_button)