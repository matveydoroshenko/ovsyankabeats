import re
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.inline.admin.admin_keyboard import admin
from loader import dp, db
from funcs.homework_defining import homework_defining


@dp.message_handler(CommandStart(deep_link=re.compile("task_")))
async def start_deeplink(message: types.Message):
    await message.delete()
    args = str(message.get_args())
    if message.from_user.id not in ADMINS:
        number = int(args[-1:])
        task_files = await db.select_task(number=number)
        await homework_defining(photo=task_files.get("photo") ,
                                file=task_files.get("file"),
                                text=task_files.get("text"),
                                video=task_files.get("video"),
                                chat_id=message.from_user.id)
    else:
        await message.answer("У админов нет домашнего задания!", reply_markup=admin)
