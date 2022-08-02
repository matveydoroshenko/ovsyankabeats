from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from funcs.deeplink import get_deeplink


def task_list(tasks_list):
    keyboard = InlineKeyboardMarkup(row_width=5)
    for task in tasks_list:
        button = InlineKeyboardButton(text=f"{task}", callback_data=f"task_id: {task}")
        keyboard.insert(button)
    cancel_button = InlineKeyboardButton(text="Отмена ❌", callback_data="cancel")
    keyboard.row(cancel_button)
    return keyboard


async def create_deeplink(task):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Домашнее задание", url=await get_deeplink(task_number=task))
    keyboard.insert(button)
    return keyboard


perform_task_keyboard = \
    InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Выполнить задание", callback_data="perform_task")]])
