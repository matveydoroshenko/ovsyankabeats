from loader import dp, db
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.admin.admin_keyboard import admin
from keyboards.inline.admin.cancel_keyboard import cancel
from states.admin.product_states import Product


@dp.callback_query_handler(text="product_photo")
async def product_photo_button(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    video = data.get("product_video")
    if video is None:
        await Product.photo.set()
        await call.message.edit_reply_markup()
        result = await call.message.edit_text("Отправь фото для товара: ", reply_markup=cancel)
        await state.update_data(message_id_product_photo=result.message_id)
        return
    await call.answer("Ты уже указал видео!", show_alert=True)


@dp.callback_query_handler(text="product_video")
async def product_video_button(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    photo = data.get("product_photo")
    if photo is None:
        await Product.video.set()
        await call.message.edit_reply_markup()
        result = await call.message.edit_text("Отправь видео для товара: ", reply_markup=cancel)
        await state.update_data(message_id_product_video=result.message_id)
        return
    await call.answer("Ты уже указал фото!", show_alert=True)


@dp.callback_query_handler(text="product_file")
async def product_file_button(call: CallbackQuery, state: FSMContext):
    await Product.file.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь файл для товара: ", reply_markup=cancel)
    await state.update_data(message_id_product_file=result.message_id)


@dp.callback_query_handler(text="product_description")
async def product_description_button(call: CallbackQuery, state: FSMContext):
    await Product.description.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь описание для товара: ", reply_markup=cancel)
    await state.update_data(message_id_product_description=result.message_id)


@dp.callback_query_handler(text="product_title")
async def product_title_button(call: CallbackQuery, state: FSMContext):
    await Product.title.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь название товара: ", reply_markup=cancel)
    await state.update_data(message_id_product_title=result.message_id)


@dp.callback_query_handler(text="product_price")
async def product_price_button(call: CallbackQuery, state: FSMContext):
    await Product.price.set()
    await call.message.edit_reply_markup()
    result = await call.message.edit_text("Отправь цену для товара: ", reply_markup=cancel)
    await state.update_data(message_id_product_price=result.message_id)


@dp.callback_query_handler(text="product_save")
async def product_save_button(call: CallbackQuery, state: FSMContext):
    count = await db.count_users()
    data = await state.get_data()
    photo = data.get("product_photo")
    video = data.get("product_video")
    file = data.get("product_file")
    description = data.get("product_description")
    title = data.get("product_title")
    price = data.get("product_price")
    if photo is None and video is None and file is None and description is None and title is None and price is None:
        await call.answer("Ты ничего не указал!", show_alert=True)
    elif photo is None and video is None:
        await call.answer("Ты не указал видео или фото!", show_alert=True)
    elif file is None:
        await call.answer("Ты не указал файл!", show_alert=True)
    elif price is None:
        await call.answer("Ты не указал цену!", show_alert=True)
    elif description is None:
        await call.answer("Ты не указал описание!", show_alert=True)
    elif title is None:
        await call.answer("Ты не указал название!", show_alert=True)
    else:
        await db.add_product(photo=photo,
                       video=video,
                       file=file,
                       description=description,
                       title=title,
                       price=price)
        await call.answer("Продукт успешно сохранён!", show_alert=True)
        text = (f"Привет, админ: {call.message.chat.full_name}!",
                f"В базе данных <b>{count}</b> пользователей",
                "Панель администратора: ")
        await call.message.edit_text("\n".join(text))
        await call.message.edit_reply_markup(admin)
        await state.reset_state()
