from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

task = InlineKeyboardMarkup()

photo_button = InlineKeyboardButton(text="Фото 📸", callback_data="task_photo")
video_button = InlineKeyboardButton(text="Видео 📹", callback_data="task_video")
text_button = InlineKeyboardButton(text="Текст 💬", callback_data="task_text")
file_button = InlineKeyboardButton(text="Файл 🗂", callback_data="task_file")
save_button = InlineKeyboardButton(text="Сохранить задание 📱", callback_data="save_task")
back_button = InlineKeyboardButton(text="Назад 🔙", callback_data="task_back")

task.row(photo_button, video_button)
task.row(text_button, file_button)
task.row(save_button)
task.row(back_button)
