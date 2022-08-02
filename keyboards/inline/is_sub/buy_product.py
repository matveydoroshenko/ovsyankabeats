from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.is_sub.product_names_factory import product


already = InlineKeyboardMarkup()

already_bought = InlineKeyboardButton(text="Уже куплено ✅", callback_data="already_bought")
back = InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_choose_product")

already.row(already_bought)
already.row(back)

def product_buy(index):
    keyboard = InlineKeyboardMarkup()
    purchase = InlineKeyboardButton(text="Купить 🛒", callback_data=product.new(index=index))
    keyboard.row(purchase)
    keyboard.row(back)
    return keyboard


