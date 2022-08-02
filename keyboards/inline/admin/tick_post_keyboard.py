import keyboards.inline.admin.post_keyboard as btn
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


photo_tick_button = InlineKeyboardButton(text="Фото ✅", callback_data="post_photo_tick")
video_tick_button = InlineKeyboardButton(text="Видео ✅", callback_data="post_video_tick")
file_tick_button = InlineKeyboardButton(text="Файл ✅", callback_data="post_file_tick")
text_tick_button = InlineKeyboardButton(text="Текст ✅", callback_data="post_text_tick")
attach_task_tick_button = InlineKeyboardButton(text="Прикрепить задание ✅", callback_data="post_attach_task_tick")

tick_photo_keyboard = InlineKeyboardMarkup()

tick_photo_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_keyboard.row(btn.text_button, btn.file_button)
tick_photo_keyboard.row(btn.attach_task_button)
tick_photo_keyboard.row(btn.send_button)
tick_photo_keyboard.row(btn.back_button)

tick_video_keyboard = InlineKeyboardMarkup()

tick_video_keyboard.row(btn.photo_button, video_tick_button)
tick_video_keyboard.row(btn.text_button, btn.file_button)
tick_video_keyboard.row(btn.attach_task_button)
tick_video_keyboard.row(btn.send_button)
tick_video_keyboard.row(btn.back_button)

tick_file_keyboard = InlineKeyboardMarkup()

tick_file_keyboard.row(btn.photo_button, btn.video_button)
tick_file_keyboard.row(btn.text_button, file_tick_button)
tick_file_keyboard.row(btn.attach_task_button)
tick_file_keyboard.row(btn.send_button)
tick_file_keyboard.row(btn.back_button)

tick_text_keyboard = InlineKeyboardMarkup()

tick_text_keyboard.row(btn.photo_button, btn.video_button)
tick_text_keyboard.row(text_tick_button, btn.file_button)
tick_text_keyboard.row(btn.attach_task_button)
tick_text_keyboard.row(btn.send_button)
tick_text_keyboard.row(btn.back_button)

tick_task_keyboard = InlineKeyboardMarkup()

tick_task_keyboard.row(btn.photo_button, btn.video_button)
tick_task_keyboard.row(btn.text_button, btn.file_button)
tick_task_keyboard.row(attach_task_tick_button)
tick_task_keyboard.row(btn.send_button)
tick_task_keyboard.row(btn.back_button)

tick_photo_video_keyboard = InlineKeyboardMarkup()

tick_photo_video_keyboard.row(photo_tick_button, video_tick_button)
tick_photo_video_keyboard.row(btn.text_button, btn.file_button)
tick_photo_video_keyboard.row(btn.attach_task_button)
tick_photo_video_keyboard.row(btn.send_button)
tick_photo_video_keyboard.row(btn.back_button)

tick_photo_file_keyboard = InlineKeyboardMarkup()

tick_photo_file_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_file_keyboard.row(btn.text_button, file_tick_button)
tick_photo_file_keyboard.row(btn.attach_task_button)
tick_photo_file_keyboard.row(btn.send_button)
tick_photo_file_keyboard.row(btn.back_button)

tick_photo_text_keyboard = InlineKeyboardMarkup()

tick_photo_text_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_text_keyboard.row(text_tick_button, btn.file_button)
tick_photo_text_keyboard.row(btn.attach_task_button)
tick_photo_text_keyboard.row(btn.send_button)
tick_photo_text_keyboard.row(btn.back_button)

tick_photo_task_keyboard = InlineKeyboardMarkup()

tick_photo_task_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_task_keyboard.row(btn.text_button, btn.file_button)
tick_photo_task_keyboard.row(attach_task_tick_button)
tick_photo_task_keyboard.row(btn.send_button)
tick_photo_task_keyboard.row(btn.back_button)

tick_video_file_keyboard = InlineKeyboardMarkup()

tick_video_file_keyboard.row(btn.photo_button, video_tick_button)
tick_video_file_keyboard.row(btn.text_button, file_tick_button)
tick_video_file_keyboard.row(btn.attach_task_button)
tick_video_file_keyboard.row(btn.send_button)
tick_video_file_keyboard.row(btn.back_button)

tick_video_text_keyboard = InlineKeyboardMarkup()

tick_video_text_keyboard.row(btn.photo_button, video_tick_button)
tick_video_text_keyboard.row(text_tick_button, btn.file_button)
tick_video_text_keyboard.row(btn.attach_task_button)
tick_video_text_keyboard.row(btn.send_button)
tick_video_text_keyboard.row(btn.back_button)

tick_video_task_keyboard = InlineKeyboardMarkup()

tick_video_task_keyboard.row(btn.photo_button, video_tick_button)
tick_video_task_keyboard.row(btn.text_button, btn.file_button)
tick_video_task_keyboard.row(attach_task_tick_button)
tick_video_task_keyboard.row(btn.send_button)
tick_video_task_keyboard.row(btn.back_button)

tick_file_text_keyboard = InlineKeyboardMarkup()

tick_file_text_keyboard.row(btn.photo_button, btn.video_button)
tick_file_text_keyboard.row(text_tick_button, file_tick_button)
tick_file_text_keyboard.row(btn.attach_task_button)
tick_file_text_keyboard.row(btn.send_button)
tick_file_text_keyboard.row(btn.back_button)

tick_file_task_keyboard = InlineKeyboardMarkup()

tick_file_task_keyboard.row(btn.photo_button, btn.video_button)
tick_file_task_keyboard.row(btn.text_button, file_tick_button)
tick_file_task_keyboard.row(attach_task_tick_button)
tick_file_task_keyboard.row(btn.send_button)
tick_file_task_keyboard.row(btn.back_button)

tick_text_task_keyboard = InlineKeyboardMarkup()

tick_text_task_keyboard.row(btn.photo_button, btn.video_button)
tick_text_task_keyboard.row(text_tick_button, btn.file_button)
tick_text_task_keyboard.row(attach_task_tick_button)
tick_text_task_keyboard.row(btn.send_button)
tick_text_task_keyboard.row(btn.back_button)

tick_photo_video_file_keyboard = InlineKeyboardMarkup()

tick_photo_video_file_keyboard.row(photo_tick_button, video_tick_button)
tick_photo_video_file_keyboard.row(btn.text_button, file_tick_button)
tick_photo_video_file_keyboard.row(btn.attach_task_button)
tick_photo_video_file_keyboard.row(btn.send_button)
tick_photo_video_file_keyboard.row(btn.back_button)

tick_photo_video_text_keyboard = InlineKeyboardMarkup()

tick_photo_video_text_keyboard.row(photo_tick_button, video_tick_button)
tick_photo_video_text_keyboard.row(text_tick_button, btn.file_button)
tick_photo_video_text_keyboard.row(btn.attach_task_button)
tick_photo_video_text_keyboard.row(btn.send_button)
tick_photo_video_text_keyboard.row(btn.back_button)

tick_photo_video_task_keyboard = InlineKeyboardMarkup()

tick_photo_video_task_keyboard.row(photo_tick_button, video_tick_button)
tick_photo_video_task_keyboard.row(btn.text_button, btn.file_button)
tick_photo_video_task_keyboard.row(attach_task_tick_button)
tick_photo_video_task_keyboard.row(btn.send_button)
tick_photo_video_task_keyboard.row(btn.back_button)

tick_photo_file_text_keyboard = InlineKeyboardMarkup()

tick_photo_file_text_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_file_text_keyboard.row(text_tick_button, file_tick_button)
tick_photo_file_text_keyboard.row(btn.attach_task_button)
tick_photo_file_text_keyboard.row(btn.send_button)
tick_photo_file_text_keyboard.row(btn.back_button)

tick_photo_file_task_keyboard = InlineKeyboardMarkup()

tick_photo_file_task_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_file_task_keyboard.row(btn.text_button, file_tick_button)
tick_photo_file_task_keyboard.row(attach_task_tick_button)
tick_photo_file_task_keyboard.row(btn.send_button)
tick_photo_file_task_keyboard.row(btn.back_button)

tick_photo_text_task_keyboard = InlineKeyboardMarkup()

tick_photo_text_task_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_text_task_keyboard.row(text_tick_button, btn.file_button)
tick_photo_text_task_keyboard.row(attach_task_tick_button)
tick_photo_text_task_keyboard.row(btn.send_button)
tick_photo_text_task_keyboard.row(btn.back_button)

tick_video_file_text_keyboard = InlineKeyboardMarkup()

tick_video_file_text_keyboard.row(btn.photo_button, video_tick_button)
tick_video_file_text_keyboard.row(text_tick_button, file_tick_button)
tick_video_file_text_keyboard.row(btn.attach_task_button)
tick_video_file_text_keyboard.row(btn.send_button)
tick_video_file_text_keyboard.row(btn.back_button)

tick_video_file_task_keyboard = InlineKeyboardMarkup()

tick_video_file_task_keyboard.row(btn.photo_button, video_tick_button)
tick_video_file_task_keyboard.row(btn.text_button, file_tick_button)
tick_video_file_task_keyboard.row(attach_task_tick_button)
tick_video_file_task_keyboard.row(btn.send_button)
tick_video_file_task_keyboard.row(btn.back_button)

tick_video_text_task_keyboard = InlineKeyboardMarkup()

tick_video_text_task_keyboard.row(btn.photo_button, video_tick_button)
tick_video_text_task_keyboard.row(text_tick_button, btn.file_button)
tick_video_text_task_keyboard.row(attach_task_tick_button)
tick_video_text_task_keyboard.row(btn.send_button)
tick_video_text_task_keyboard.row(btn.back_button)

tick_file_text_task_keyboard = InlineKeyboardMarkup()

tick_file_text_task_keyboard.row(btn.photo_button, btn.video_button)
tick_file_text_task_keyboard.row(text_tick_button, file_tick_button)
tick_file_text_task_keyboard.row(attach_task_tick_button)
tick_file_text_task_keyboard.row(btn.send_button)
tick_file_text_task_keyboard.row(btn.back_button)

tick_photo_video_file_text_keyboard = InlineKeyboardMarkup()

tick_photo_video_file_text_keyboard.row(photo_tick_button, video_tick_button)
tick_photo_video_file_text_keyboard.row(text_tick_button, file_tick_button)
tick_photo_video_file_text_keyboard.row(btn.attach_task_button)
tick_photo_video_file_text_keyboard.row(btn.send_button)
tick_photo_video_file_text_keyboard.row(btn.back_button)

tick_photo_video_file_task_keyboard = InlineKeyboardMarkup()

tick_photo_video_file_text_keyboard.row(photo_tick_button, video_tick_button)
tick_photo_video_file_text_keyboard.row(btn.text_button, file_tick_button)
tick_photo_video_file_text_keyboard.row(attach_task_tick_button)
tick_photo_video_file_text_keyboard.row(btn.send_button)
tick_photo_video_file_text_keyboard.row(btn.back_button)

tick_photo_video_text_task_keyboard = InlineKeyboardMarkup()

tick_photo_video_text_task_keyboard.row(photo_tick_button, video_tick_button)
tick_photo_video_text_task_keyboard.row(text_tick_button, btn.file_button)
tick_photo_video_text_task_keyboard.row(attach_task_tick_button)
tick_photo_video_text_task_keyboard.row(btn.send_button)
tick_photo_video_text_task_keyboard.row(btn.back_button)

tick_photo_file_text_task_keyboard = InlineKeyboardMarkup()

tick_photo_file_text_task_keyboard.row(photo_tick_button, btn.video_button)
tick_photo_file_text_task_keyboard.row(text_tick_button, file_tick_button)
tick_photo_file_text_task_keyboard.row(attach_task_tick_button)
tick_photo_file_text_task_keyboard.row(btn.send_button)
tick_photo_file_text_task_keyboard.row(btn.back_button)

tick_video_file_text_task_keyboard = InlineKeyboardMarkup()

tick_video_file_text_keyboard.row(btn.photo_button, video_tick_button)
tick_video_file_text_keyboard.row(text_tick_button, file_tick_button)
tick_video_file_text_keyboard.row(attach_task_tick_button)
tick_video_file_text_keyboard.row(btn.send_button)
tick_video_file_text_keyboard.row(btn.back_button)

tick_all_keyboard = InlineKeyboardMarkup()

tick_all_keyboard.row(photo_tick_button, video_tick_button)
tick_all_keyboard.row(text_tick_button, file_tick_button)
tick_all_keyboard.row(attach_task_tick_button)
tick_all_keyboard.row(btn.send_button)
tick_all_keyboard.row(btn.back_button)
