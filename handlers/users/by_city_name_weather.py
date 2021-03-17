from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.utils.markdown import hbold
from keyboards.default import send_geolocation
from keyboards.inline import greeting_inline_menu, now_several_days_choice, number_of_days_choice
import emoji
from weather_api import geo, city, new_weather
from states import PushButton
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


# Выбор погоды по названию города
@dp.callback_query_handler(text="city_name_weather")
async def by_city_name_weather(call: CallbackQuery):
    await call.message.answer(text="Введи название города")
    await call.message.edit_reply_markup()
    await PushButton.after_push_city_button.set()

# Выдача погоды по названию города
@dp.message_handler(content_types=['text'], state=PushButton.after_push_city_button)
async def answer_after_write_city_name(message: types.Message, state: FSMContext):
    try:
        text = city(city_name=message.text)
        await message.answer(text=text, reply_markup=send_geolocation)
        await state.finish()
    except Exception as exc:
        await message.answer(f'Не знаю такой город... '
                             f'. Попробуй ввести новый населенный пункт', reply_markup=send_geolocation)