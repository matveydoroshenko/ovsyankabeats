import aioschedule as aioschedule
from loader import db, bot


async def morning_users():
    id_list = await db.select_all_users_id()
    for chat_id in id_list:
        for id in chat_id:
            await bot.send_message(chat_id=id, text="Доброе утро ☀️")


async def evening_users():
    id_list = await db.select_all_users_id()
    for chat_id in id_list:
        for id in chat_id:
            await bot.send_message(chat_id=id, text="Спокойной ночи 🌙")


async def main():
    aioschedule.every().day.at('10:00').do(morning_users)
    aioschedule.every().day.at('22:00').do(evening_users)

    while True:
        await aioschedule.run_pending()