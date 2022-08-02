from datetime import datetime, timedelta
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink
from data import config
from data.items import items
from keyboards.inline.is_sub.is_sub_keyboard import is_sub
from keyboards.inline.no_sub.link_keyboard import link_keyboard
from keyboards.inline.no_sub.no_sub_keyboard import no_sub
from keyboards.inline.no_sub.purchases_keyboard import paid_keyboard
from loader import dp, db, bot
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney


@dp.callback_query_handler(text_contains="buy:")
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    item_id = call.data.split(":")[-1]
    item_id = int(item_id) - 1
    item = items[item_id]

    amount = item.price
    payment = Payment(amount=amount)
    payment.create()

    await call.message.edit_text(
        text="\n".join([
            f"Оплатите {amount:.2f} по ссылке",
            "",
            hlink(config.WALLET_QIWI, url=payment.invoice),
            ""
        ]),
        reply_markup=paid_keyboard)

    await state.set_state("qiwi")
    await state.update_data(payment=payment)

    @dp.callback_query_handler(text="cancel_payment", state="qiwi")
    async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
        await call.message.edit_text("Отменено", reply_markup=no_sub)
        await state.finish()

    @dp.callback_query_handler(text="paid", state="qiwi")
    async def approve_payment(call: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        payment: Payment = data.get("payment")
        try:
            payment.check_payment()
        except NoPaymentFound:
            await call.answer("Транзакция не найдена.", show_alert=True)
            return
        except NotEnoughMoney:
            await call.answer("Оплаченная сумма меньше необходимой.", show_alert=True)
            return
        else:
            await db.add_user(user_id=call.message.forward_from.id,
                        name=call.message.forward_from.full_name,
                        username=call.message.forward_from.username,
                        date=str(call.message.date))
            await db.add_user_files(user_id=call.message.forward_from.id,
                              file="[]")
            await db.add_user_balance(user_id=call.message.forward_from.id,
                                gem_amount=0)
            link = await bot.create_chat_invite_link(chat_id=-1001791355844,
                                                     expire_date=datetime.now() + timedelta(days=1),
                                                     member_limit=1)
            await call.message.edit_text(text=f"Привет, {call.message.chat.full_name}!",
                                         reply_markup=link_keyboard(link=str(link.invite_link)))
            await call.message.answer(f"Привет, {call.message.chat.id}!", reply_markup=is_sub)
        await state.finish()
