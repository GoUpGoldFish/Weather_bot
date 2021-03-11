from aiogram.dispatcher.filters.state import StatesGroup, State


class PushButton(StatesGroup):
    after_push_city_button = State()
    get_geolocation_weather_now = State()
    get_geolocation_weather_for_1_day = State()
    get_geolocation_weather_for_2_day = State()
    get_geolocation_weather_for_3_day = State()
    get_geolocation_weather_for_4_day = State()
    get_geolocation_weather_for_5_day = State()
    get_geolocation_weather_for_6_day = State()
    get_geolocation_weather_for_7_day = State()