from aiogram.dispatcher.filters.state import State, StatesGroup


class Product(StatesGroup):
    photo = State()
    video = State()
    file = State()
    description = State()
    title = State()
    price = State()
