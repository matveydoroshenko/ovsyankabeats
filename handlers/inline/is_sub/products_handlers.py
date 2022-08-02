import ast
from loader import dp, db
from aiogram.types import CallbackQuery
from keyboards.inline.is_sub.product_names_factory import product_names, product
from keyboards.inline.is_sub.buy_product import product_buy, already
from keyboards.inline.is_sub.product_keyboard import choose_product
from keyboards.inline.is_sub.is_sub_keyboard import is_sub


@dp.callback_query_handler(product_names.filter())
async def product_names_buttons(call: CallbackQuery, callback_data: dict):
    index = int(callback_data.get("index"))
    product = await db.select_product(number=index)
    files = await db.select_user_files(user_id=call.message.chat.id)
    files = ast.literal_eval(str(files.get("file")))
    if str(index) in files:
        reply_markup = already
    else:
        reply_markup = product_buy(index=index)
    text = (f"Название: {product[4]}",
            "",
            f"Цена: {product[6]} 💵",
            "",
            "Описание:",
            "",
            f"{product[5]}")
    if product[1] is None:
        await call.message.delete()
        await call.message.answer_video(video=product[2],
                                        caption="\n".join(text),
                                        reply_markup=reply_markup)
    elif product[2] is None:
        await call.message.delete()
        await call.message.answer_photo(photo=product[1],
                                        caption="\n".join(text),
                                        reply_markup=reply_markup)


@dp.callback_query_handler(product.filter())
async def buy_product_button(call: CallbackQuery, callback_data: dict):
    gem_amount = await db.select_gem_amount(user_id=call.message.chat.id)
    gem_amount = int(gem_amount.get("gem_amount"))
    index = int(callback_data.get("index"))
    product = await db.select_product(number=index)
    gem_amount = gem_amount - int(product[6])
    if gem_amount >= 0:
        await call.message.delete()
        await db.update_gem_amount(gem_amount=gem_amount, user_id=call.message.chat.id)
        await call.message.answer_document(document=product[3], reply_markup=is_sub)
        files = await db.select_user_files(user_id=call.message.chat.id)
        files = ast.literal_eval(str(files.get("file")))
        files.append(str(index))
        files = str(files)
        await db.update_user_files(user_id=call.message.chat.id, file=files)
        await call.answer("Товар успешно куплен!", show_alert=True)
        return
    await call.answer("Не хватает денег!", show_alert=True)

@dp.callback_query_handler(text="back_to_choose_product")
async def back_to_choose_product(call: CallbackQuery):
    await call.message.delete()
    titles = await db.select_all_products_title()
    products = []
    for title in titles:
        products.append(title[0])
    await call.message.answer(text="Выбери продукт: ", reply_markup=choose_product(products=products))
