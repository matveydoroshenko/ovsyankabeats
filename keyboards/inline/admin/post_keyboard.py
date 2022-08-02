from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

post = InlineKeyboardMarkup()

photo_button = InlineKeyboardButton(text="Фото 📸", callback_data="post_photo")
video_button = InlineKeyboardButton(text="Видео 📹", callback_data="post_video")
text_button = InlineKeyboardButton(text="Текст 💬", callback_data="post_text")
file_button = InlineKeyboardButton(text="Файл 🗂", callback_data="post_file")
attach_task_button = InlineKeyboardButton(text="Прикрепить задание 📎", callback_data="post_attach_task")
send_button = InlineKeyboardButton(text="Отправить пост 📱", callback_data="post_send")
back_button = InlineKeyboardButton(text="Назад 🔙", callback_data="post_back")

post.row(photo_button, video_button)
post.row(text_button, file_button)
post.row(attach_task_button)
post.row(send_button)
post.row(back_button)
