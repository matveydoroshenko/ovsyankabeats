from loader import bot
from keyboards.inline.admin.assess_keyboard import assess_keyboard
from keyboards.inline.admin.assess_keyboard import assess_keyboard_tick


async def assessment_respond_defining(content_type, file, text, chat_id, user_id):
    if text == 'None':
        if content_type == 'photo':
            await bot.send_photo(chat_id=chat_id, photo=file, reply_markup=assess_keyboard(user_id=user_id))
        elif content_type == 'video':
            await bot.send_video(chat_id=chat_id, video=file, reply_markup=assess_keyboard(user_id=user_id))
        elif content_type == 'document':
            await bot.send_document(chat_id=chat_id, document=file, reply_markup=assess_keyboard(user_id=user_id))
        elif content_type == 'audio':
            await bot.send_audio(chat_id=chat_id, audio=file, reply_markup=assess_keyboard(user_id=user_id))
        elif content_type == 'voice':
            await bot.send_voice(chat_id=chat_id, voice=file, reply_markup=assess_keyboard(user_id=user_id))
        elif content_type == 'video_note':
            await bot.send_video_note(chat_id=chat_id, video_note=file, reply_markup=assess_keyboard(user_id=user_id))
    else:
        if content_type == 'photo':
            await bot.send_photo(chat_id=chat_id, photo=file, reply_markup=assess_keyboard(user_id=user_id),
                                 caption=text)
        elif content_type == 'video':
            await bot.send_video(chat_id=chat_id, video=file, reply_markup=assess_keyboard(user_id=user_id),
                                 caption=text)
        elif content_type == 'document':
            await bot.send_document(chat_id=chat_id, document=file, reply_markup=assess_keyboard(user_id=user_id),
                                    caption=text)
        elif content_type == 'audio':
            await bot.send_audio(chat_id=chat_id, audio=file, reply_markup=assess_keyboard(user_id=user_id),
                                 caption=text)
        elif content_type == 'voice':
            await bot.send_voice(chat_id=chat_id, voice=file, reply_markup=assess_keyboard(user_id=user_id),
                                 caption=text)
        elif content_type == 'text':
            await bot.send_message(chat_id=chat_id, text=text, reply_markup=assess_keyboard(user_id=user_id))


async def assessment_respond_defining_tick(content_type, file, text, chat_id, user_id):
    if text == 'None':
        if content_type == 'photo':
            await bot.send_photo(chat_id=chat_id, photo=file, reply_markup=assess_keyboard_tick(user_id=user_id))
        elif content_type == 'video':
            await bot.send_video(chat_id=chat_id, video=file, reply_markup=assess_keyboard_tick(user_id=user_id))
        elif content_type == 'document':
            await bot.send_document(chat_id=chat_id, document=file, reply_markup=assess_keyboard_tick(user_id=user_id))
        elif content_type == 'audio':
            await bot.send_audio(chat_id=chat_id, audio=file, reply_markup=assess_keyboard_tick(user_id=user_id))
        elif content_type == 'voice':
            await bot.send_voice(chat_id=chat_id, voice=file, reply_markup=assess_keyboard_tick(user_id=user_id))
        elif content_type == 'video_note':
            await bot.send_video_note(chat_id=chat_id, video_note=file,
                                      reply_markup=assess_keyboard_tick(user_id=user_id))
    else:
        if content_type == 'photo':
            await bot.send_photo(chat_id=chat_id, photo=file, reply_markup=assess_keyboard_tick(user_id=user_id),
                                 caption=text)
        elif content_type == 'video':
            await bot.send_video(chat_id=chat_id, video=file, reply_markup=assess_keyboard_tick(user_id=user_id),
                                 caption=text)
        elif content_type == 'document':
            await bot.send_document(chat_id=chat_id, document=file, reply_markup=assess_keyboard_tick(user_id=user_id),
                                    caption=text)
        elif content_type == 'audio':
            await bot.send_audio(chat_id=chat_id, audio=file, reply_markup=assess_keyboard_tick(user_id=user_id),
                                 caption=text)
        elif content_type == 'voice':
            await bot.send_voice(chat_id=chat_id, voice=file, reply_markup=assess_keyboard_tick(user_id=user_id),
                                 caption=text)
        elif content_type == 'text':
            await bot.send_message(chat_id=chat_id, text=text, reply_markup=assess_keyboard_tick(user_id=user_id))
