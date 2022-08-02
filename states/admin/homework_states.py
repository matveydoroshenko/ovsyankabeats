from aiogram.dispatcher.filters.state import State, StatesGroup


class UserRespond(StatesGroup):
    user_respond = State()
