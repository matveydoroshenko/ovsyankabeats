from aiogram.dispatcher.filters.state import State, StatesGroup


class Task(StatesGroup):
    photo = State()
    video = State()
    file = State()
    text = State()
