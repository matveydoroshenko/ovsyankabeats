from aiogram.dispatcher.filters.state import StatesGroup, State


class AddUser(StatesGroup):
    message = State()
