from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.is_sub.product_names_factory import product_names
from keyboards.inline.is_sub.back_to_is_sub_keyboard import back_button


def choose_product(products):
    keyboard = InlineKeyboardMarkup()
    for index, name in enumerate(products):
        button = InlineKeyboardButton(text=f"{name}", callback_data=product_names.new(index=index + 1))
        keyboard.row(button)
    keyboard.row(back_button)
    return keyboard
