from loader import bot
from keyboards.inline.admin.homework_keyboard import perform_task_keyboard


async def homework_defining(photo: object, video: object, file: object, text: object, chat_id: object) -> object:
    if photo is None and video is None and file is None and text is not None:
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=perform_task_keyboard)
    elif photo is None and video is None and file is not None and text is None:
        await bot.send_document(chat_id=chat_id, document=file, reply_markup=perform_task_keyboard)
    elif photo is None and video is not None and file is None and text is None:
        await bot.send_video(chat_id=chat_id, video=video, reply_markup=perform_task_keyboard)
    elif photo is not None and video is None and file is None and text is None:
        await bot.send_photo(chat_id=chat_id, photo=photo, reply_markup=perform_task_keyboard)
    elif photo is None and video is None and file is not None and text is not None:
        await bot.send_document(chat_id=chat_id, document=file, caption=text, reply_markup=perform_task_keyboard)
    elif photo is None and video is not None and file is None and text is not None:
        await bot.send_video(chat_id=chat_id, video=video, caption=text, reply_markup=perform_task_keyboard)
    elif photo is None and video is not None and file is not None and text is None:
        await bot.send_video(chat_id=chat_id, video=video)
        await bot.send_document(chat_id=chat_id, document=file, reply_markup=perform_task_keyboard)
    elif photo is not None and video is None and file is None and text is not None:
        await bot.send_photo(chat_id=chat_id, photo=photo, caption=text, reply_markup=perform_task_keyboard)
    elif photo is not None and video is None and file is not None and text is None:
        await bot.send_photo(chat_id=chat_id, photo=photo)
        await bot.send_document(chat_id=chat_id, document=file, reply_markup=perform_task_keyboard)
    elif photo is not None and video is not None and file is None and text is None:
        await bot.send_photo(chat_id=chat_id, photo=photo)
        await bot.send_video(chat_id=chat_id, video=video, reply_markup=perform_task_keyboard)
    elif photo is None and video is not None and file is not None and text is not None:
        await bot.send_video(chat_id=chat_id, video=video)
        await bot.send_document(chat_id=chat_id, document=file, caption=text, reply_markup=perform_task_keyboard)
    elif photo is not None and video is None and file is not None and text is not None:
        await bot.send_document(chat_id=chat_id, document=file)
        await bot.send_photo(chat_id=chat_id, photo=photo, caption=text, reply_markup=perform_task_keyboard)
    elif photo is not None and video is not None and file is None and text is not None:
        await bot.send_photo(chat_id=chat_id, photo=photo)
        await bot.send_video(chat_id=chat_id, video=video, caption=text, reply_markup=perform_task_keyboard)
    elif photo is not None and video is None and file is not None and text is None:
        await bot.send_photo(chat_id=chat_id, photo=photo)
        await bot.send_video(chat_id=chat_id, video=video)
        await bot.send_document(chat_id=chat_id, document=file, reply_markup=perform_task_keyboard)
    elif photo is not None and video is not None and file is not None and text is not None:
        await bot.send_document(chat_id=chat_id, document=file)
        await bot.send_photo(chat_id=chat_id, photo=photo)
        await bot.send_video(chat_id=chat_id, video=video, caption=text, reply_markup=perform_task_keyboard)
