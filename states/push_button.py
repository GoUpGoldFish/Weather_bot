from aiogram.dispatcher.filters.state import StatesGroup, State


class PushButtonCity(StatesGroup):
    after_push_city_button = State()