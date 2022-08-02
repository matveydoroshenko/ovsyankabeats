from loader import dp, db
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from funcs import keyboard_defining
from funcs.assessment_respond_defining import assessment_respond_defining
from keyboards.inline.admin.admin_keyboard import admin


@dp.callback_query_handler(text="cancel", state="*")
async def cancel(call: CallbackQuery, state: FSMContext):
    current_state = str(await state.get_state())
    count = await db.count_users()
    data = await state.get_data()
    if current_state.startswith("AddUser"):
        text = (f"Привет, админ: {call.message.chat.full_name}!",
                f"В базе данных <b>{count}</b> пользователей",
                "Панель администратора: ")
        await call.message.edit_text("\n".join(text))
        await call.message.edit_reply_markup(admin)
        await state.reset_state()
    elif current_state.startswith("Post"):
        photo = data.get("post_photo")
        video = data.get("post_video")
        file = data.get("post_file")
        text = data.get("post_text")
        task = data.get("post_task")
        reply_markup = keyboard_defining.post_keyboard_defining(photo=photo,
                                                                    video=video,
                                                                    file=file,
                                                                    text=text,
                                                                    task=task)
        await call.message.edit_text(text="Выбери категорию: ", reply_markup=reply_markup)
        await state.reset_state(with_data=False)
    elif current_state.startswith("Product"):
        photo = data.get("product_photo")
        video = data.get("product_video")
        file = data.get("product_file")
        description = data.get("product_description")
        title = data.get("product_title")
        price = data.get("product_price")
        reply_markup = keyboard_defining.product_keyboard_defining(photo=photo,
                                                                    video=video,
                                                                    file=file,
                                                                    description=description,
                                                                    title=title,
                                                                    price=price)
        await call.message.edit_text(text="Выбери категорию: ", reply_markup=reply_markup)
        await state.reset_state(with_data=False)
    elif current_state.startswith("Task"):
        photo = data.get("task_photo")
        text = data.get("task_text")
        file = data.get("task_file")
        video = data.get("task_video")
        reply_markup = keyboard_defining.task_keyboard_defining(photo=photo,
                                                                    video=video,
                                                                    file=file,
                                                                    text=text)
        await call.message.edit_text(text="Выбери категорию: ", reply_markup=reply_markup)
        await state.reset_state(with_data=False)
    elif current_state.startswith("Post"):
        photo = data.get("post_photo")
        video = data.get("post_video")
        file = data.get("post_file")
        text = data.get("post_text")
        task = data.get("post_task")
        reply_markup = keyboard_defining.post_keyboard_defining(photo=photo,
                                                                video=video,
                                                                file=file,
                                                                text=text,
                                                                task=task)
        await call.message.edit_text(text="Выбери категорию: ", reply_markup=reply_markup)
        await state.reset_state(with_data=False)
    elif current_state.startswith("Comment"):
        await call.message.delete()
        user_responds = db.select_all_users_responds()
        respond = user_responds[0]
        user_id, file, content_type, text = str(respond[0]), str(respond[1]), str(respond[2]), str(respond[3])
        await assessment_respond_defining(file=file,
                                          content_type=content_type,
                                          text=text,
                                          chat_id=call.message.chat.id,
                                          user_id=user_id)