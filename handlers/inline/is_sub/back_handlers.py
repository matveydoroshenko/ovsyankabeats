import ast
from loader import dp, bot
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.is_sub.is_sub_keyboard import is_sub


@dp.callback_query_handler(text="back_to_is_sub")
async def back_to_is_sub(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    messages = ast.literal_eval(str(data.get("messages_back_to_is_sub")))
    for msg in messages:
        await bot.delete_message(chat_id=call.message.chat.id,
                                 message_id=msg)
        await call.message.answer(f"Привет, {call.message.chat.full_name}!", reply_markup=is_sub)


@dp.callback_query_handler(text="back_to_product")
async def back_to_product(call: CallbackQuery):
    await call.message.edit_text(f"Привет, {call.message.chat.full_name}!", reply_markup=is_sub)




