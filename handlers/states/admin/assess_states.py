from loader import dp, db, bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from states.admin.comment_state import Comment
from funcs.assessment_respond_defining import assessment_respond_defining_tick


@dp.message_handler(state=Comment.comment)
async def comment_button_states(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    message_id = data.get("message_id_comment_respond")
    await bot.delete_message(chat_id=message.chat.id, message_id=message_id)
    await state.update_data(respond_comment=message.text)
    user_responds = await db.select_all_users_responds()
    respond = user_responds[0]
    user_id, file, content_type, text = str(respond.get("user_id")), \
                                        str(respond.get("file")), \
                                        str(respond.get("content_type")), \
                                        str(respond.get("text"))
    await assessment_respond_defining_tick(file=file,
                                           content_type=content_type,
                                           text=text,
                                           chat_id=message.chat.id,
                                           user_id=user_id)
    await state.reset_state(with_data=False)
