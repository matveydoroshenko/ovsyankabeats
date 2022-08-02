from loader import bot, dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.admin.add_user_state import AddUser
from keyboards.inline.admin.admin_keyboard import admin


@dp.message_handler(state=AddUser.message)
async def add_user_state(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.delete()
    await bot.delete_message(message_id=data.get("message_id_add_user_instruction"),
                             chat_id=message.from_user.id)
    if message.from_user.username is None:
        text_user = ('Пользователь успешно добавлен!',
                     f'ID: {message.forward_from.id}',
                     f'Имя: {message.from_user.full_name}',
                     f'Дата добавления: {message.date}')
    else:
        text_user = ('Пользователь успешно добавлен!',
                     f'ID: {message.forward_from.id}',
                     f'Имя: {message.forward_from.full_name}',
                     f'Username: @{message.forward_from.username}',
                     f'Дата добавления: {message.date}')
    await db.add_user(user_id=message.forward_from.id,
                name=message.forward_from.full_name,
                username=message.forward_from.username,
                date=str(message.date))
    await db.add_user_files(user_id=message.forward_from.id,
                      file="[]")
    await db.add_user_balance(user_id=message.forward_from.id,
                        gem_amount=0)
    count = await db.count_users()
    text_admin = (f"Привет, админ: {message.chat.full_name}!",
                  f"В базе данных <b>{count}</b> пользователей",
                  "Панель администратора: ")
    await message.answer("\n".join(text_user))
    await message.answer("\n".join(text_admin), reply_markup=admin)
    await state.finish()
