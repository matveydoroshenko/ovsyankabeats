import os

import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from funcs.assessment_respond_defining import assessment_respond_defining
from funcs.users_txt import create_users_txt
from keyboards.inline.admin.admin_keyboard import admin
from keyboards.inline.admin.cancel_keyboard import cancel
from keyboards.inline.admin.post_keyboard import post
from keyboards.inline.admin.product_keyboard import product
from keyboards.inline.admin.task_keyboard import task
from loader import dp, db
from states.admin.add_user_state import AddUser


@dp.callback_query_handler(text="add_user")
async def add_user_button(call: CallbackQuery, state: FSMContext):
    await AddUser.message.set()
    text = (
        "<b>1.</b> Спроси пользователя разрешил ли он пересылку сообщений",
        "",
        "<b>2. Настройки -> Конфиденциальность -> Пересылка сообщений -> Все </b>",
        "",
        "<b>3.</b> Перешли текстовое сообщение пользователя боту"
    )
    try:
        result = await call.message.edit_text(text="\n".join(text), reply_markup=cancel)
    except aiogram.utils.exceptions.BadRequest:
        await call.message.delete()
        result = await call.message.answer("\n".join(text))
    await state.update_data(message_id_add_user_instruction=result.message_id)


@dp.callback_query_handler(text="list_of_users")
async def list_of_users_button(call: CallbackQuery):
    await call.message.delete()
    list_of_users = await db.select_all_users()
    create_users_txt(list_of_users=list_of_users)
    await call.message.answer_document(open("data/users.txt", "rb"),
                                       caption="Список пользователей",
                                       reply_markup=admin)
    os.remove("data/users.txt")


@dp.callback_query_handler(text="create_post")
async def create_post_button(call: CallbackQuery):
    try:
        await call.message.edit_text("Выбери категорию: ")
        await call.message.edit_reply_markup(post)
    except aiogram.utils.exceptions.BadRequest:
        await call.message.delete()
        await call.message.answer("Выбери категорию: ", reply_markup=post)


@dp.callback_query_handler(text="create_task")
async def create_task_button(call: CallbackQuery):
    try:
        await call.message.edit_text("Выбери категорию: ")
        await call.message.edit_reply_markup(task)
    except aiogram.utils.exceptions.BadRequest:
        await call.message.delete()
        await call.message.answer("Выбери категорию: ", reply_markup=task)


@dp.callback_query_handler(text="create_product")
async def create_product_button(call: CallbackQuery):
    try:
        await call.message.edit_text(text="Выбери категорию: ", reply_markup=product)
    except aiogram.utils.exceptions.BadRequest:
        await call.message.delete()
        await call.message.answer("Выбери категорию: ", reply_markup=product)


@dp.callback_query_handler(text="check_tasks")
async def check_tasks_button(call: CallbackQuery):
    user_responds = await db.select_all_users_responds()
    if user_responds:
        await call.message.delete()
        respond = user_responds[0]
        user_id, file, content_type, text = str(respond.get("user_id")), \
                                            str(respond.get("file")), \
                                            str(respond.get("content_type")), \
                                            str(respond.get("text"))
        await assessment_respond_defining(file=file,
                                          content_type=content_type,
                                          text=text,
                                          chat_id=call.message.chat.id,
                                          user_id=user_id)

    elif not user_responds:
        await call.answer("Нет работ пользователей!", show_alert=True)
