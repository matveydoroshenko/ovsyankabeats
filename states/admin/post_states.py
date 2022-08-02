from aiogram.dispatcher.filters.state import State, StatesGroup


class Post(StatesGroup):
    photo = State()
    video = State()
    file = State()
    text = State()
