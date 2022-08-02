from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

product = InlineKeyboardMarkup()

photo_button = InlineKeyboardButton(text="Фото 📸", callback_data="product_photo")
video_button = InlineKeyboardButton(text="Видео 📹", callback_data="product_video")
file_button = InlineKeyboardButton(text="Файл 🗂", callback_data="product_file")
description_button = InlineKeyboardButton(text="Описание 💬", callback_data="product_description")
title_button = InlineKeyboardButton(text="Название 📒", callback_data="product_title")
price_button = InlineKeyboardButton(text="Цена 💰", callback_data="product_price")
save_button = InlineKeyboardButton(text="Cохранить товар 🏬", callback_data="product_save")
back_button = InlineKeyboardButton(text="Назад 🔙", callback_data="post_back")

product.row(photo_button, video_button)
product.row(description_button, file_button)
product.row(title_button, price_button)
product.row(save_button)
product.row(back_button)