import ast
import aiogram
from loader import dp, db
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.no_sub.back_keybaord import back
from keyboards.inline.is_sub.product_keyboard import choose_product
from keyboards.inline.is_sub.back_to_is_sub_keyboard import back_to_is_sub


@dp.callback_query_handler(text="shop_is_sub")
async def shop_is_sub(call: CallbackQuery):
    titles = await db.select_all_products_title()
    products = []
    for title in titles:
        products.append(title[0])
    try:
        await call.message.edit_text(text="Выбери продукт: ", reply_markup=choose_product(products=products))
    except aiogram.utils.exceptions.BadRequest:
        await call.message.delete()
        await call.message.answer(text="Выбери продукт: ", reply_markup=choose_product(products=products))


@dp.callback_query_handler(text="profile_is_sub")
async def profile_is_sub(call: CallbackQuery):
    gem_amount = await db.select_gem_amount(user_id=call.message.chat.id)
    gem_amount = gem_amount.get("gem_amount")
    name = call.message.chat.full_name
    username = call.message.chat.username
    if username is None:
        text = (f"Имя: {name}",
                f"Баланс: {gem_amount} 💵")
    elif gem_amount is None:
        text = (f"Имя: {name}",
                f"Юзернейм: @{username}",
                "У тебя нет 💵")
    elif username is None and gem_amount is None:
        text = (f"Имя: {name}",
                "У тебя нет 💵")
    else:
        text = (f"Имя: {name}",
                f"Юзернейм: @{username}",
                f"Баланс: {gem_amount} 💵")
    await call.message.edit_text(text="\n".join(text), reply_markup=back)


@dp.callback_query_handler(text="purchases_is_sub")
async def purchases_is_sub(call: CallbackQuery, state: FSMContext):
    messages = []
    files = await db.select_user_files(user_id=call.message.chat.id)
    files = files[0]
    if files == '[]':
        await call.answer("У тебя нет покупок!", show_alert=True)
        return
    await call.message.delete()
    products = await db.select_user_files(user_id=call.message.chat.id)
    products = ast.literal_eval(str(products.get("file")))
    for index, product in enumerate(products):
        file = await db.select_product_file(number=product)
        if index + 1 != len(products):
            message = await call.message.answer_document(document=file)
        elif index + 1 == len(products):
            message = await call.message.answer_document(document=file, reply_markup=back_to_is_sub)
        messages.append(message.message_id)
    await state.update_data(messages_back_to_is_sub=messages)
