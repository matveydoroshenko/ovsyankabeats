from loader import dp, db
from aiogram.types import CallbackQuery
from keyboards.inline.no_sub.no_sub_keyboard import no_sub
from keyboards.inline.is_sub.is_sub_keyboard import is_sub


@dp.callback_query_handler(text="back_button_no_sub")
async def back_no_sub_button(call: CallbackQuery):
    user_data = await db.select_user(user_id=call.message.chat.id)
    if user_data is None:
        await call.message.edit_text(text=f"Привет, {call.message.chat.full_name}!", reply_markup=no_sub)
    elif user_data is not None:
        await call.message.edit_text(text=f"Привет, {call.message.chat.full_name}!", reply_markup=is_sub)