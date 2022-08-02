from loader import dp
from aiogram.types import CallbackQuery
from data.items import items
from keyboards.inline.no_sub.back_keybaord import back
from keyboards.inline.no_sub.purchases_keyboard import buy_keyboard


@dp.callback_query_handler(text="about_course")
async def about_course_button(call: CallbackQuery):
    await call.message.edit_text(text="Пример текста о курсе", reply_markup=back)


@dp.callback_query_handler(text="buy_course")
async def show_items(call: CallbackQuery):
    text = ("Название продукта: {title}",
            "",
            "Цена: {price:.2f} <b>RUB</b>",
            )

    for item in items:
        await call.message.edit_text(
            text="\n".join(text).format(
                title=item.title,
                price=item.price,
            ),
            reply_markup=buy_keyboard(item_id=item.id)
        )
