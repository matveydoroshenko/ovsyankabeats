from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from funcs.keyboard_defining import post_keyboard_defining
from states.admin.post_states import Post


@dp.message_handler(state=Post.photo, content_types=types.ContentType.PHOTO)
async def post_photo_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = message.photo[-1].file_id
    video = data.get("post_video")
    file = data.get("post_file")
    text = data.get("post_text")
    task = data.get("post_task")
    message_id = data.get("message_id_post_photo")
    await state.update_data(post_photo=photo)
    reply_markup = post_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text,
                                          task=task)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)

@dp.message_handler(state=Post.video, content_types=types.ContentType.VIDEO)
async def post_video_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("post_photo")
    video = message.video.file_id
    file = data.get("post_file")
    text = data.get("post_text")
    task = data.get("post_task")
    message_id = data.get("message_id_post_video")
    await state.update_data(post_video=video)
    reply_markup = post_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text,
                                          task=task)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)

@dp.message_handler(state=Post.file, content_types=types.ContentType.DOCUMENT)
async def post_file_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("post_photo")
    video = data.get("post_video")
    file = message.document.file_id
    text = data.get("post_text")
    task = data.get("post_task")
    message_id = data.get("message_id_post_file")
    await state.update_data(post_file=file)
    reply_markup = post_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text,
                                          task=task)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)

@dp.message_handler(state=Post.text, content_types=types.ContentType.TEXT)
async def post_video_text(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("post_photo")
    video = data.get("post_video")
    file = data.get("post_file")
    text = message.text
    task = data.get("post_task")
    message_id = data.get("message_id_post_text")
    await state.update_data(post_text=text)
    reply_markup = post_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text,
                                          task=task)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)
