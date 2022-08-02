from keyboards.inline.admin.cancel_keyboard import cancel
from loader import dp, db
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.admin.admin_keyboard import admin
from states.admin.task_states import Task
from states.admin.homework_states import UserRespond


@dp.callback_query_handler(text="task_back")
async def task_back_button(call: CallbackQuery, state: FSMContext):
    count = await db.count_users()
    text: tuple[str, str, str] = (f"Привет, админ: {call.message.from_user.full_name}!",
                                  f"В базе данных <b>{count}</b> пользователей",
                                  "Панель администратора: ")
    await call.message.edit_text("\n".join(text))
    await call.message.edit_reply_markup(admin)
    await state.reset_state()


@dp.callback_query_handler(text="task_photo")
async def task_photo_button(call: CallbackQuery, state: FSMContext):
    await Task.photo.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь фото для задания: ", reply_markup=cancel)
    await state.update_data(message_id_task_photo=result.message_id)


@dp.callback_query_handler(text="task_video")
async def task_video_button(call: CallbackQuery, state: FSMContext):
    await Task.video.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь видео для задания: ", reply_markup=cancel)
    await state.update_data(message_id_task_video=result.message_id)


@dp.callback_query_handler(text="task_file")
async def task_file_button(call: CallbackQuery, state: FSMContext):
    await Task.file.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь файл для задания: ", reply_markup=cancel)
    await state.update_data(message_id_task_file=result.message_id)


@dp.callback_query_handler(text="task_text")
async def task_text_button(call: CallbackQuery, state: FSMContext):
    await Task.text.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь текст для задания: ", reply_markup=cancel)
    await state.update_data(message_id_task_text=result.message_id)


@dp.callback_query_handler(text="save_task")
async def save_task_button(call: CallbackQuery, state: FSMContext):
    count = await db.count_users()
    data = await state.get_data()
    photo = data.get("task_photo")
    text = data.get("task_text")
    file = data.get("task_file")
    video = data.get("task_video")
    if photo is None and video is None and file is None and text is None:
        await call.answer("Ты ничего не указал!", show_alert=True)
    else:
        await db.add_task(photo=photo,
                    text=text,
                    file=file,
                    video=video)
        await call.answer("Задание успешно сохранено!", show_alert=True)
        text = (f"Привет, админ: {call.message.chat.full_name}!",
                f"В базе данных <b>{count}</b> пользователей",
                "Панель администратора: ")
        await call.message.edit_text("\n".join(text))
        await call.message.edit_reply_markup(admin)
        await state.reset_state()


@dp.callback_query_handler(text="perform_task")
async def perform_task_button(call: CallbackQuery, state: FSMContext):
    await UserRespond.user_respond.set()
    await call.message.edit_reply_markup()
    text_message_1 = ("Отправь свою работу:",
                      "Если надо подпиши")
    message_1 = await call.message.answer("\n".join(text_message_1))
    await state.update_data(message_id_1_perform_task=message_1.message_id)
    await state.update_data(chat_id_1_perform_task=message_1.chat.id)

