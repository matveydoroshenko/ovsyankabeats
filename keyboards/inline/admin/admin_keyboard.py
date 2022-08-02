from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin: InlineKeyboardMarkup = InlineKeyboardMarkup()

add_user_button = InlineKeyboardButton(text="Добавить юзера ➕", callback_data="add_user")
list_of_users_button = InlineKeyboardButton(text="Список юзеров 📄", callback_data="list_of_users")
create_post_button = InlineKeyboardButton(text="Создать пост ⌨️", callback_data="create_post")
create_task_button = InlineKeyboardButton(text="Создать задание 📚", callback_data="create_task")
create_product_button = InlineKeyboardButton(text="Создать товар 📒", callback_data="create_product")
check_tasks_button = InlineKeyboardButton(text="Проверить задания 📖", callback_data="check_tasks")

admin.row(add_user_button, list_of_users_button)
admin.row(create_post_button, create_task_button)
admin.row(create_product_button)
admin.row(check_tasks_button)
