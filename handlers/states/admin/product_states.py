from loader import dp, bot
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext
from funcs.keyboard_defining import product_keyboard_defining
from states.admin.product_states import Product


@dp.message_handler(state=Product.photo, content_types=ContentType.PHOTO)
async def product_photo_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = message.photo[-1].file_id
    video = data.get("product_video")
    file = data.get("product_file")
    description = data.get("product_description")
    title = data.get("product_title")
    price = data.get("product_price")
    message_id = data.get("message_id_product_photo")
    await state.update_data(product_photo=photo)
    reply_markup = product_keyboard_defining(photo=photo,
                                             video=video,
                                             file=file,
                                             description=description,
                                             title=title,
                                             price=price)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Product.video, content_types=ContentType.VIDEO)
async def product_video_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("product_photo")
    video = message.video.file_id
    file = data.get("product_file")
    description = data.get("product_description")
    title = data.get("product_title")
    price = data.get("product_price")
    message_id = data.get("message_id_product_video")
    await state.update_data(product_video=video)
    reply_markup = product_keyboard_defining(photo=photo,
                                             video=video,
                                             file=file,
                                             description=description,
                                             title=title,
                                             price=price)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Product.file, content_types=ContentType.DOCUMENT)
async def product_file_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("product_photo")
    video = data.get("product_video")
    file = message.document.file_id
    description = data.get("product_description")
    title = data.get("product_title")
    price = data.get("product_price")
    message_id = data.get("message_id_product_file")
    await state.update_data(product_file=file)
    reply_markup = product_keyboard_defining(photo=photo,
                                             video=video,
                                             file=file,
                                             description=description,
                                             title=title,
                                             price=price)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Product.description, content_types=ContentType.TEXT)
async def product_description_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("product_photo")
    video = data.get("product_video")
    file = data.get("product_file")
    description = message.text
    title = data.get("product_title")
    price = data.get("product_price")
    message_id = data.get("message_id_product_description")
    await state.update_data(product_description=description)
    reply_markup = product_keyboard_defining(photo=photo,
                                             video=video,
                                             file=file,
                                             description=description,
                                             title=title,
                                             price=price)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Product.title, content_types=ContentType.TEXT)
async def product_title_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("product_photo")
    video = data.get("product_video")
    file = data.get("product_file")
    description = data.get("product_description")
    title = message.text
    price = data.get("product_price")
    message_id = data.get("message_id_product_title")
    await state.update_data(product_title=title)
    reply_markup = product_keyboard_defining(photo=photo,
                                             video=video,
                                             file=file,
                                             description=description,
                                             title=title,
                                             price=price)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)


@dp.message_handler(state=Product.price, content_types=ContentType.TEXT)
async def product_price_state(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    photo = data.get("product_photo")
    video = data.get("product_video")
    file = data.get("product_file")
    description = data.get("product_description")
    title = data.get("product_title")
    price = message.text
    message_id = data.get("message_id_product_price")
    await state.update_data(product_price=price)
    reply_markup = product_keyboard_defining(photo=photo,
                                             video=video,
                                             file=file,
                                             description=description,
                                             title=title,
                                             price=price)
    await bot.edit_message_text(text="Выберите категорию: ",
                                message_id=message_id,
                                chat_id=message.from_user.id,
                                reply_markup=reply_markup)
    await state.reset_state(with_data=False)