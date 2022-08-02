from funcs.assessment_respond_defining import assessment_respond_defining
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.admin.comment_state import Comment
from keyboards.inline.admin.assess_callback_factory import assess_callback
from keyboards.inline.admin.cancel_keyboard import cancel
from keyboards.inline.admin.admin_keyboard import admin


@dp.callback_query_handler(assess_callback.filter(choice="tick"))
async def assess_tick_button(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    user_id = int(callback_data.get("user_id"))
    gem_amount = await db.select_gem_amount(user_id=user_id)
    gem_amount = int(gem_amount.get("gem_amount"))
    count = await db.count_users()
    await db.update_gem_amount(gem_amount=gem_amount + 50, user_id=user_id)
    comment = data.get("respond_comment")
    if comment is not None:
        text = ("Ты правильно выполнил задание ✅",
                "И получил 50 💵",
                "",
                "<i>Комментарий от админа:</i>",
                "",
                f"{comment}")
        await bot.send_message(chat_id=user_id, text="\n".join(text))
    else:
        text = ("Ты правильно выполнил задание ✅",
                "И получил 50 💵")
        await bot.send_message(chat_id=user_id,text="\n".join(text))
    await db.delete_respond(user_id=user_id)
    user_responds = await db.select_all_users_responds()
    if len(user_responds) > 0:
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

    elif len(user_responds) == 0:
        await call.answer("Ты проверил все задания!", show_alert=True)
        text = (f"Привет, админ: {call.message.from_user.full_name}!",
                f"В базе данных <b>{count}</b> пользователей",
                "Панель администратора: ")
        await call.message.answer("\n".join(text), reply_markup=admin)


@dp.callback_query_handler(assess_callback.filter(choice="cross"))
async def assess_cross_button(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    user_id = int(callback_data.get("user_id"))
    comment = data.get("respond_comment")
    count = await db.count_users()
    if comment is not None:
        text = ("Ты неправильно выполнил задание ❌",
                "Ты не получил сегодня 💵",
                "",
                "<i>Комментарий от админа:</i>",
                "",
                f"{comment}")
        await bot.send_message(chat_id=user_id, text="\n".join(text))
    else:
        text = ("Ты неправильно выполнил задание ❌",
                "Ты не получил сегодня 💵")
        await bot.send_message(chat_id=user_id,text="\n".join(text))
    await db.delete_respond(user_id=user_id)
    user_responds = await db.select_all_users_responds()
    if len(user_responds) > 0:
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
    elif len(user_responds) == 0:
        await call.answer("Ты проверил все задания!", show_alert=True)
        text = (f"Привет, админ: {call.message.from_user.full_name}!",
                f"В базе данных <b>{count}</b> пользователей",
                "Панель администратора: ")
        await call.message.answer("\n".join(text), reply_markup=admin)


@dp.callback_query_handler(text="comment_button")
async def assess_comment_button(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Comment.comment.set()
    message_id = await call.message.answer("Введи комментарий о работе: ", reply_markup=cancel)
    await state.update_data(message_id_comment_respond=message_id.message_id)
