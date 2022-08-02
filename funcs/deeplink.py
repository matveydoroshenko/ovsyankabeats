from aiogram.utils.deep_linking import get_start_link


async def get_deeplink(task_number):
    link = await get_start_link(f'task_{int(task_number)}', encode=False)
    return link
