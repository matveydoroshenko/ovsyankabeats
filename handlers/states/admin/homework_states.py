import aiogram
import pymorphy2
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.is_sub.is_sub_keyboard import is_sub
from states.admin.homework_states import UserRespond
from funcs.user_respond_content_type_define import define_content_type
from loader import dp, db, bot


@dp.message_handler(state=UserRespond.user_respond, content_types=types.ContentType.ANY)
async def user_respond_catch(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_id_1 = data.get("message_id_1_perform_task")
    chat_id_1 = data.get("chat_id_1_perform_task")
    await message.delete()
    try:
        await bot.delete_message(chat_id=chat_id_1, message_id=message_id_1)
        user_id = message.from_user.id
        content_type = message.content_type
        file = define_content_type(content_type=content_type, message=message)
        text = message.caption
        await db.add_user_respond(user_id=user_id,
                            content_type=content_type,
                            file=file,
                            text=text)
        await message.answer("Получил и сохранил твою работу!")
        await message.answer(f"Привет, {message.chat.full_name}!", reply_markup=is_sub)
        await state.reset_state(with_data=False)
    except aiogram.utils.exceptions.MessageToDeleteNotFound:
        if str(message.text).startswith("/start task_"):
            await message.answer("Ты уже выполнил задание!")


