from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from funcs.keyboard_defining import post_keyboard_defining


@dp.callback_query_handler(text_contains="task_id: ")
async def choose_task(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    photo = data.get("post_photo")
    video = data.get("post_video")
    file = data.get("post_file")
    text = data.get("post_text")
    task = str(call.data)[-2:]
    message_id = data.get("message_id_post_attach_task")
    await state.update_data(post_task=task)
    reply_markup = post_keyboard_defining(photo=photo,
                                          video=video,
                                          file=file,
                                          text=text,
                                          task=task)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=call.message.chat.id,
                                reply_markup=reply_markup)
