import asyncio
import logging
from loader import db
from utils.set_bot_commands import set_default_commands
from funcs.schedule_funcs import main


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)
    logging.info("Подключился к базе данных!")
    logging.info("Создаю таблицы!")
    await db.create_table_balance()
    await db.create_table_homework()
    await db.create_table_products()
    await db.create_table_user_files()
    await db.create_table_user_respond()
    await db.create_table_users()
    logging.info("Готово!")

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
