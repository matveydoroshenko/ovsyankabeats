def define_content_type(content_type, message):
    if content_type == 'audio':
        file = message.audio.file_id
    elif content_type == 'document':
        file = message.document.file_id
    elif content_type == 'voice':
        file = message.voice.file_id
    elif content_type == 'video':
        file = message.video.file_id
    elif content_type == 'video_note':
        file = message.video_note.file_id
    elif content_type == 'photo':
        file = message.photo[-1].file_id
    return file