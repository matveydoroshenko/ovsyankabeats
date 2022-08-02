from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

no_sub = InlineKeyboardMarkup()

buy_access = InlineKeyboardButton(text="Купить курс 🛒", callback_data="buy_course")
info = InlineKeyboardButton(text="О курсе ℹ️", callback_data="about_course")

no_sub.row(buy_access, info)
