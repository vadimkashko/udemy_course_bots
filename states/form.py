from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    before_name = State()
    before_email = State()
    before_phone = State()
