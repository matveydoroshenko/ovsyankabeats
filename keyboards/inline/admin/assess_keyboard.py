from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.admin.assess_callback_factory import assess_callback
from keyboards.inline.admin.post_keyboard import back_button


def assess_keyboard(user_id):
    keyboard = InlineKeyboardMarkup()

    tick = InlineKeyboardButton(text="✅", callback_data=assess_callback.new(choice='tick', user_id=user_id))
    cross = InlineKeyboardButton(text="❌", callback_data=assess_callback.new(choice='cross', user_id=user_id))
    comment = InlineKeyboardButton(text="Прокомментировать ⌨️", callback_data="comment_button")

    keyboard.row(tick, cross)
    keyboard.row(comment)
    keyboard.row(back_button)

    return keyboard


def assess_keyboard_tick(user_id):
    keyboard = InlineKeyboardMarkup()

    tick = InlineKeyboardButton(text="✅", callback_data=assess_callback.new(choice='tick', user_id=user_id))
    cross = InlineKeyboardButton(text="❌", callback_data=assess_callback.new(choice='cross', user_id=user_id))
    comment = InlineKeyboardButton(text="Комментарий ✅", callback_data="comment_button_tick")

    keyboard.row(tick, cross)
    keyboard.row(comment)
    keyboard.row(back_button)

    return keyboard
