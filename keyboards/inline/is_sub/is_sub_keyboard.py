from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


is_sub = InlineKeyboardMarkup()

shop = InlineKeyboardButton(text="Магазин 🛒", callback_data="shop_is_sub")
profile = InlineKeyboardButton(text="Профиль 💾", callback_data="profile_is_sub")
purchases = InlineKeyboardButton(text="Покупки 🛍", callback_data="purchases_is_sub")

is_sub.row(shop, profile)
is_sub.row(purchases)