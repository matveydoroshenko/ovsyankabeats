from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.inline.admin.admin_keyboard import admin
from keyboards.inline.no_sub.no_sub_keyboard import no_sub
from keyboards.inline.is_sub.is_sub_keyboard import is_sub
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    count = await db.count_users()
    user_data = await db.select_user(user_id=message.chat.id)
    if message.chat.id in ADMINS:
        text = (f"Привет, админ: {message.from_user.full_name}!",
                f"В базе данных <b>{count}</b> пользователей",
                "Панель администратора: ")
        await message.answer("\n".join(text), reply_markup=admin)
    elif user_data is None:
        await message.answer(f"Привет, {message.chat.full_name}!", reply_markup=no_sub)
    elif user_data is not None:
        await message.answer(f"Привет, {message.chat.full_name}!", reply_markup=is_sub)
