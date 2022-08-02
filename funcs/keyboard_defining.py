def post_keyboard_defining(photo, video, file, text, task):
    import keyboards.inline.admin.tick_post_keyboard as kb
    from keyboards.inline.admin.post_keyboard import post
    if photo is None and video is None and file is None and text is None and task is None:
        reply_markup = post
    elif photo is None and video is None and file is None and text is None and task is not None:
        reply_markup = kb.tick_task_keyboard
    elif photo is None and video is None and file is None and text is not None and task is None:
        reply_markup = kb.tick_text_keyboard
    elif photo is None and video is None and file is not None and text is None and task is None:
        reply_markup = kb.tick_file_keyboard
    elif photo is None and video is not None and file is None and text is None and task is None:
        reply_markup = kb.tick_video_keyboard
    elif photo is not None and video is None and file is None and text is None and task is None:
        reply_markup = kb.tick_photo_keyboard
    elif photo is None and video is None and file is None and text is not None and task is not None:
        reply_markup = kb.tick_text_task_keyboard
    elif photo is None and video is None and file is not None and text is None and task is not None:
        reply_markup = kb.tick_file_task_keyboard
    elif photo is None and video is None and file is not None and text is not None and task is None:
        reply_markup = kb.tick_file_text_keyboard
    elif photo is None and video is not None and file is None and text is None and task is not None:
        reply_markup = kb.tick_video_task_keyboard
    elif photo is None and video is not None and file is None and text is not None and task is None:
        reply_markup = kb.tick_video_text_keyboard
    elif photo is None and video is not None and file is not None and text is None and task is None:
        reply_markup = kb.tick_video_file_keyboard
    elif photo is not None and video is None and file is None and text is None and task is not None:
        reply_markup = kb.tick_photo_task_keyboard
    elif photo is not None and video is None and file is None and text is not None and task is None:
        reply_markup = kb.tick_photo_text_keyboard
    elif photo is not None and video is None and file is not None and text is None and task is None:
        reply_markup = kb.tick_photo_file_keyboard
    elif photo is not None and video is not None and file is None and text is None and task is None:
        reply_markup = kb.tick_photo_video_keyboard
    elif photo is None and video is None and file is not None and text is not None and task is not None:
        reply_markup = kb.tick_file_text_task_keyboard
    elif photo is None and video is not None and file is None and text is not None and task is not None:
        reply_markup = kb.tick_video_text_task_keyboard
    elif photo is None and video is not None and file is not None and text is None and task is not None:
        reply_markup = kb.tick_video_file_task_keyboard
    elif photo is None and video is not None and file is not None and text is not None and task is None:
        reply_markup = kb.tick_video_file_text_keyboard
    elif photo is not None and video is None and file is None and text is not None and task is not None:
        reply_markup = kb.tick_photo_text_task_keyboard
    elif photo is not None and video is None and file is not None and text is None and task is not None:
        reply_markup = kb.tick_photo_file_task_keyboard
    elif photo is not None and video is None and file is not None and text is not None and task is None:
        reply_markup = kb.tick_photo_file_text_keyboard
    elif photo is not None and video is not None and file is None and text is None and task is not None:
        reply_markup = kb.tick_photo_video_task_keyboard
    elif photo is not None and video is not None and file is None and text is not None and task is None:
        reply_markup = kb.tick_photo_video_text_keyboard
    elif photo is not None and video is not None and file is not None and text is None and task is None:
        reply_markup = kb.tick_photo_video_file_keyboard
    elif photo is None and video is not None and file is not None and text is not None and task is not None:
        reply_markup = kb.tick_video_file_text_task_keyboard
    elif photo is not None and video is None and file is not None and text is not None and task is not None:
        reply_markup = kb.tick_photo_file_text_task_keyboard
    elif photo is not None and video is not None and file is None and text is not None and task is not None:
        reply_markup = kb.tick_photo_video_text_task_keyboard
    elif photo is not None and video is not None and file is not None and text is None and task is not None:
        reply_markup = kb.tick_photo_video_file_task_keyboard
    elif photo is not None and video is not None and file is not None and text is not None and task is None:
        reply_markup = kb.tick_photo_video_file_text_keyboard
    elif photo is not None and video is not None and file is not None and text is not None and task is not None:
        reply_markup = kb.tick_all_keyboard
    return reply_markup


def task_keyboard_defining(photo, video, file, text):
    import keyboards.inline.admin.tick_task_keyboard as kb
    from keyboards.inline.admin.task_keyboard import task
    if photo is None and video is None and file is None and text is None:
        reply_markup = task
    elif photo is None and video is None and file is None:
        reply_markup = kb.tick_text_keyboard
    elif photo is None and video is None and text is None:
        reply_markup = kb.tick_file_keyboard
    elif photo is None and file is None and text is None:
        reply_markup = kb.tick_video_keyboard
    elif video is None and file is None and text is None:
        reply_markup = kb.tick_photo_keyboard
    elif photo is None and video is None:
        reply_markup = kb.tick_file_text_keyboard
    elif photo is None and file is None:
        reply_markup = kb.tick_video_text_keyboard
    elif photo is None and text is None:
        reply_markup = kb.tick_video_file_keyboard
    elif video is None and file is None:
        reply_markup = kb.tick_photo_text_keyboard
    elif video is None and text is None:
        reply_markup = kb.tick_photo_file_keyboard
    elif file is None and text is None:
        reply_markup = kb.tick_photo_video_keyboard
    elif photo is None:
        reply_markup = kb.tick_video_file_text_keyboard
    elif video is None:
        reply_markup = kb.tick_photo_file_text_keyboard
    elif file is None:
        reply_markup = kb.tick_photo_video_text_keyboard
    elif text is None:
        reply_markup = kb.tick_photo_video_file_keyboard
    elif photo is not None and video is not None and file is not None and text is not None:
        reply_markup = kb.tick_all_keyboard
    return reply_markup


def product_keyboard_defining(photo, video, file, description, title, price):
    import keyboards.inline.admin.tick_product_keyboard as kb
    from keyboards.inline.admin.product_keyboard import product
    if photo is None and video is None and file is None and description is None and title is None and price is None:
        reply_markup = product
    elif photo is None and video is None and file is None and description is None and title is None:
        reply_markup = kb.tick_price_keyboard
    elif photo is None and video is None and file is None and description is None and price is None:
        reply_markup = kb.tick_title_keyboard
    elif photo is None and video is None and file is None and title is None and price is None:
        reply_markup = kb.tick_description_keyboard
    elif photo is None and video is None and description is None and title is None and price is None:
        reply_markup = kb.tick_file_keyboard
    elif photo is None and file is None and description is None and title is None and price is None:
        reply_markup = kb.tick_video_keyboard
    elif video is None and file is None and description is None and title is None and price is None:
        reply_markup = kb.tick_photo_keyboard
    elif photo is None and video is None and file is None and description is None:
        reply_markup = kb.tick_title_price_keyboard
    elif photo is None and video is None and file is None and title is None:
        reply_markup = kb.tick_description_price_keyboard
    elif photo is None and video is None and file is None and price is None:
        reply_markup = kb.tick_description_price_keyboard
    elif photo is None and video is None and description is None and title is None:
        reply_markup = kb.tick_file_price_keyboard
    elif photo is None and video is None and description is None and price is None:
        reply_markup = kb.tick_file_title_keyboard
    elif photo is None and video is None and title is None and price is None:
        reply_markup = kb.tick_file_description_keyboard
    elif photo is None and file is None and description is None and title is None:
        reply_markup = kb.tick_video_price_keyboard
    elif photo is None and file is None and description is None and price is None:
        reply_markup = kb.tick_video_title_keyboard
    elif photo is None and file is None and title is None and price is None:
        reply_markup = kb.tick_video_description_keyboard
    elif photo is None and description is None and title is None and price is None:
        reply_markup = kb.tick_video_file_keyboard
    elif video is None and file is None and description is None and title is None:
        reply_markup = kb.tick_photo_price_keyboard
    elif video is None and file is None and description is None and price is None:
        reply_markup = kb.tick_photo_title_keyboard
    elif video is None and title is None and description is None and price is None:
        reply_markup = kb.tick_photo_file_keyboard
    elif video is None and file is None and title is None and price is None:
        reply_markup = kb.tick_photo_description_keyboard
    elif video is None and file is None and description is None and price is None:
        reply_markup = kb.tick_photo_title_keyboard
    elif file is None and description is None and title is None and price is None:
        reply_markup = kb.tick_photo_video_keyboard
    elif photo is None and video is None and file is None is None:
        reply_markup = kb.tick_description_title_price_keyboard
    elif photo is None and video is None and description is None:
        reply_markup = kb.tick_file_title_price_keyboard
    elif photo is None and video is None and title is None:
        reply_markup = kb.tick_file_description_price_keyboard
    elif photo is None and video is None and price is None:
        reply_markup = kb.tick_file_description_title_keyboard
    elif photo is None and file is None and description is None:
        reply_markup = kb.tick_video_title_price_keyboard
    elif photo is None and file is None and title is None:
        reply_markup = kb.tick_video_description_price_keyboard
    elif photo is None and file is None and price is None:
        reply_markup = kb.tick_video_description_title_keyboard
    elif photo is None and description is None and title is None:
        reply_markup = kb.tick_video_file_price_keyboard
    elif photo is None and description is None and price is None:
        reply_markup = kb.tick_file_title_price_keyboard
    elif photo is None and title is None and price is None:
        reply_markup = kb.tick_file_description_price_keyboard
    elif video is None and file is None and description is None:
        reply_markup = kb.tick_photo_title_price_keyboard
    elif video is None and file is None and title is None:
        reply_markup = kb.tick_photo_description_price_keyboard
    elif video is None and file is None and price is None:
        reply_markup = kb.tick_photo_description_title_keyboard
    elif video is None and description is None and title is None:
        reply_markup = kb.tick_photo_file_price_keyboard
    elif video is None and description is None and price is None:
        reply_markup = kb.tick_photo_file_title_keyboard
    elif video is None and title is None and price is None:
        reply_markup = kb.tick_photo_file_description_keyboard
    elif file is None and description is None and title is None:
        reply_markup = kb.tick_photo_video_price_keyboard
    elif file is None and description is None and price is None:
        reply_markup = kb.tick_photo_video_title_keyboard
    elif file is None and title is None and price is None:
        reply_markup = kb.tick_photo_video_description_keyboard
    elif description is None and title is None and price is None:
        reply_markup = kb.tick_photo_video_file_keyboard
    elif photo is None and video is None:
        reply_markup = kb.tick_file_description_title_price_keyboard
    elif photo is None and file is None:
        reply_markup = kb.tick_video_description_title_price_keyboard
    elif photo is None and description is None:
        reply_markup = kb.tick_video_file_title_price_keyboard
    elif photo is None and title is None:
        reply_markup = kb.tick_video_file_description_price_keyboard
    elif photo is None and price is None:
        reply_markup = kb.tick_video_file_description_title_keyboard
    elif video is None and file is None:
        reply_markup = kb.tick_photo_description_title_price_keyboard
    elif video is None and description is None:
        reply_markup = kb.tick_photo_file_title_price_keyboard
    elif video is None and title is None:
        reply_markup = kb.tick_photo_file_description_price_keyboard
    elif video is None and price is None:
        reply_markup = kb.tick_photo_file_description_title_keyboard
    elif file is None and description is None:
        reply_markup = kb.tick_photo_video_title_price_keyboard
    elif file is None and title is None:
        reply_markup = kb.tick_photo_video_description_price_keyboard
    elif file is None and price is None:
        reply_markup = kb.tick_photo_video_description_title_keyboard
    elif description is None and title is None:
        reply_markup = kb.tick_photo_video_file_price_keyboard
    elif description is None and price is None:
        reply_markup = kb.tick_photo_video_file_title_keyboard
    elif title is None and price is None:
        reply_markup = kb.tick_photo_video_file_description_keyboard
    elif photo is None:
        reply_markup = kb.tick_video_file_description_title_price_keyboard
    elif video is None:
        reply_markup = kb.tick_photo_file_description_title_price_keyboard
    elif file is None:
        reply_markup = kb.tick_photo_video_description_title_price_keyboard
    elif description is None:
        reply_markup = kb.tick_photo_video_file_title_price_keyboard
    elif title is None:
        reply_markup = kb.tick_photo_video_file_description_price_keyboard
    elif price is None:
        reply_markup = kb.tick_photo_video_file_description_title_keyboard
    elif photo is not None and video is not None and file is not None and description is not None \
                                                      and title is not None and price is not None:
        reply_markup = kb.tick_all_keyboard
    return reply_markup
