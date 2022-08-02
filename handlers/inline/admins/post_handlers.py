import aiogram
from loader import db, dp
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.admin.admin_keyboard import admin
from keyboards.inline.admin.homework_keyboard import task_list
from keyboards.inline.admin.cancel_keyboard import cancel
from states.admin.post_states import Post
from funcs.post_defining import post_defining
from exceptions.post_exceptions import NoFiles


@dp.callback_query_handler(text="post_back")
async def post_back_button(call: CallbackQuery, state: FSMContext):
    count = await db.count_users()
    text = (f"Привет, админ: {call.message.chat.full_name}!",
            f"В базе данных <b>{count}</b> пользователей",
            "Панель администратора: ")
    try:
        await call.message.edit_text("\n".join(text))
        await call.message.edit_reply_markup(admin)
    except aiogram.utils.exceptions.BadRequest:
        await call.message.delete()
        await call.message.answer("\n".join(text), reply_markup=admin)
    await state.reset_state()


@dp.callback_query_handler(text="post_photo")
async def post_photo_button(call: CallbackQuery, state: FSMContext):
    await Post.photo.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь фото для поста: ", reply_markup=cancel)
    await state.update_data(message_id_post_photo=result.message_id)


@dp.callback_query_handler(text="post_video")
async def post_video_button(call: CallbackQuery, state: FSMContext):
    await Post.video.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь видео для поста: ", reply_markup=cancel)
    await state.update_data(message_id_post_video=result.message_id)


@dp.callback_query_handler(text="post_file")
async def post_file_button(call: CallbackQuery, state: FSMContext):
    await Post.file.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь файл для поста: ", reply_markup=cancel)
    await state.update_data(message_id_post_file=result.message_id)


@dp.callback_query_handler(text="post_text")
async def post_text_button(call: CallbackQuery, state: FSMContext):
    await Post.text.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь текст для поста: ", reply_markup=cancel)
    await state.update_data(message_id_post_text=result.message_id)


@dp.callback_query_handler(text="post_attach_task")
async def post_attach_task_button(call: CallbackQuery, state: FSMContext):
    count = await db.count_tasks()
    if count != 0:
        tasks_list = list(range(1, count + 1))
        result = await call.message.edit_text("Выбери задание для поста: ")
        await call.message.edit_reply_markup(task_list(tasks_list=tasks_list))
        await state.update_data(message_id_post_attach_task=result.message_id)
    else:
        await call.answer("Ты не создал задания!", show_alert=True)


@dp.callback_query_handler(text="post_send")
async def post_send_button(call: CallbackQuery, state: FSMContext):
    count = await db.count_users()
    data = await state.get_data()
    photo = data.get("post_photo")
    video = data.get("post_video")
    file = data.get("post_file")
    text = data.get("post_text")
    task = data.get("post_task")
    id_list = await db.select_all_users_id()
    for chat_id in id_list:
        for id in chat_id:
            try:
                await post_defining(photo=photo,
                                    video=video,
                                    file=file,
                                    text=text,
                                    chat_id=id,
                                    task=task)
                await call.answer("Пост успешно выложен!", show_alert=True)
            except NoFiles:
                await call.answer("Ты ничего не указал!", show_alert=True)
    text_admin = (f"Привет, админ: {call.message.chat.full_name}!",
                  f"В базе данных <b>{count}</b> пользователей",
                  "Панель администратора: ")
    await call.message.edit_text("\n".join(text_admin))
    await call.message.edit_reply_markup(admin)
    await state.reset_state(with_data=False)
