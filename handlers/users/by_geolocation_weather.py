from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.utils.markdown import hbold
from keyboards.default import choice
from keyboards.inline import greeting_inline_menu, now_several_days_choice, number_of_days_choice
import emoji
from weather_api import geo, city, new_weather
from states import PushButton
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


#Выбор погоды по геолокации
@dp.callback_query_handler(text="geolocation_weather")
async def by_geolocation_weather(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text="Я могу показать погоду:", reply_markup=now_several_days_choice)
    await call.message.edit_reply_markup()


# Погода по геолокации (нажатие кнопки "сейчас")
@dp.callback_query_handler(text="now")
async def by_geolocation_weather_now(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_now.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_now)
async def weather_by_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    text = new_weather(lat=lat, lon=lon, how_many_days=0)
    await message.answer(text=text, reply_markup=choice)
    await state.finish()


# Погода по геолокации (нажатие кнопки "на несколько дней")
@dp.callback_query_handler(text="for_several_days")
async def by_geolocation_weather_for_several_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text="Выбери на сколько дней мне показать погоду:", reply_markup=number_of_days_choice)
    await call.message.edit_reply_markup()

# Погода по геолокации (по кол-ву дней, которые выбрал пользователь из инлайн клавиатуры)
@dp.callback_query_handler(text="1_number_of_days")
async def by_geolocation_weather_for_1_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_for_1_day.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_for_1_day)
async def weather_by_location_1_days(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    text = new_weather(lat=lat, lon=lon, how_many_days=0)
    await message.answer(text=text, reply_markup=choice)
    await state.finish()


@dp.callback_query_handler(text="2_number_of_days")
async def by_geolocation_weather_for_2_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_for_2_day.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_for_2_day)
async def weather_by_location_2_days(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    for i in range(0, 2):
        text = new_weather(lat=lat, lon=lon, how_many_days=i)
        await message.answer(text=text, reply_markup=choice)
    await state.finish()


@dp.callback_query_handler(text="3_number_of_days")
async def by_geolocation_weather_for_3_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_for_3_day.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_for_3_day)
async def weather_by_location_3_days(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    for i in range(0, 3):
        text = new_weather(lat=lat, lon=lon, how_many_days=i)
        await message.answer(text=text, reply_markup=choice)
    await state.finish()


@dp.callback_query_handler(text="4_number_of_days")
async def by_geolocation_weather_for_4_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_for_4_day.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_for_4_day)
async def weather_by_location_4_days(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    for i in range(0, 4):
        text = new_weather(lat=lat, lon=lon, how_many_days=i)
        await message.answer(text=text, reply_markup=choice)
    await state.finish()


@dp.callback_query_handler(text="5_number_of_days")
async def by_geolocation_weather_for_5_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_for_5_day.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_for_5_day)
async def weather_by_location_4_days(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    for i in range(0, 5):
        text = new_weather(lat=lat, lon=lon, how_many_days=i)
        await message.answer(text=text, reply_markup=choice)
    await state.finish()


@dp.callback_query_handler(text="6_number_of_days")
async def by_geolocation_weather_for_6_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_for_6_day.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_for_6_day)
async def weather_by_location_6_days(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    for i in range(0, 6):
        text = new_weather(lat=lat, lon=lon, how_many_days=i)
        await message.answer(text=text, reply_markup=choice)
    await state.finish()


@dp.callback_query_handler(text="7_number_of_days")
async def by_geolocation_weather_for_7_days(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text='Нажми кнопку "отправить геолокацию"', reply_markup=choice)
    await call.message.edit_reply_markup()
    await PushButton.get_geolocation_weather_for_7_day.set()


@dp.message_handler(content_types=['location'], state=PushButton.get_geolocation_weather_for_7_day)
async def weather_by_location_7_days(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    for i in range(0, 7):
        text = new_weather(lat=lat, lon=lon, how_many_days=i)
        await message.answer(text=text, reply_markup=choice)
    await state.finish()

