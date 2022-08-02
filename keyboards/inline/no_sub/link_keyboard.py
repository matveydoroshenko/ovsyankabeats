from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def link_keyboard(link):
    keyboard = InlineKeyboardMarkup()
    link = InlineKeyboardButton(text="Приглашение в чат", url=f"{link}")
    keyboard.row(link)
    return keyboard