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


# Стартовое приветствие
@dp.message_handler(Command("start"))
async def start_greeting(message: types.Message):
    await message.answer('Привет ' + hbold(f'{message.chat.first_name}') + ', я погодный бот. \n\n'
                         + 'Если тебе нужно узнать погоду - я тебе помогу\n\n'
                           'Просто выбери, что тебе нужно: ', reply_markup=greeting_inline_menu)


@dp.message_handler(content_types=['text'])
async def press_menu_button(message: types.Message):
    if message.text == emoji.emojize(":wrench:", use_aliases=True) + ' меню':
        await message.answer(text="Выбери, что тебе нужно:",reply_markup=greeting_inline_menu)


# @dp.message_handler(content_types=['location'])
# async def weather_by_location(message: types.Message):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     text = new_weather(lat=lat, lon=lon, how_many_days=0) + f'Ваши координаты: {lat}, {lon}'
#     await message.answer(text=text, reply_markup=choice)
#
#
# @dp.message_handler(text=emoji.emojize(":black_nib:", use_aliases=True) + ' по названию')
# async def weather_by_write(message: types.Message):
#     await message.answer("Введите название населенного пункта", reply_markup=choice)
#     await PushButtonCity.after_push_city_button.set()
#
#
# @dp.message_handler(content_types=['text'], state=PushButtonCity.after_push_city_button)
# async def answer(message: types.Message, state: FSMContext):
#     try:
#         text = city(city_name=message.text)
#         await message.answer(text=text, reply_markup=choice)
#         await state.finish()
#     except Exception as exc:
#         await message.answer(f'Не знаю такой город... '
#                              f'. Попробуй ввести новый населенный пункт', reply_markup=choice)



# TODO добавить выбор погоды (сейчас, на день, на неделю). Дописать функции апи - передавать в функцию вариант в качестве аргумента
# TODO Текст вывода разнообразить emoji
# TODO Добавить модуль смены языка (реализовать через состояние)
# TODO Возможность администрирования бота через анминскую кансоль - через пароль лого, смена тайтла, дискрипшина и т.д.)
# TODO Убрать форматирование финальной строки
# TODO Сделать округление температуры до целых чисел