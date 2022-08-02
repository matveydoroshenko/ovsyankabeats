from loader import dp, bot
from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.admin.task_states import Task
from funcs.keyboard_defining import task_keyboard_defining


@dp.message_handler(state=Task.photo, content_types=types.ContentType.PHOTO)
async def task_photo_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = message.photo[-1].file_id
    video = data.get("task_video")
    file = data.get("task_file")
    text = data.get("task_text")
    message_id = data.get("message_id_task_photo")
    await state.update_data(task_photo=photo)
    reply_markup = task_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Task.video, content_types=types.ContentType.VIDEO)
async def task_video_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("task_photo")
    video = message.video.file_id
    file = data.get("task_file")
    text = data.get("task_text")
    message_id = data.get("message_id_task_video")
    await state.update_data(task_video=video)
    reply_markup = task_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Task.file, content_types=types.ContentType.DOCUMENT)
async def task_file_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("task_photo")
    video = data.get("task_video")
    file = message.document.file_id
    text = data.get("task_text")
    message_id = data.get("message_id_task_file")
    await state.update_data(task_file=file)
    reply_markup = task_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Task.text, content_types=types.ContentType.TEXT)
async def task_text_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("task_photo")
    text = message.text
    file = data.get("task_file")
    video = data.get("task_video")
    message_id = data.get("message_id_task_text")
    await state.update_data(task_text=text)
    reply_markup = task_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)
