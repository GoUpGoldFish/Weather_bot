from loader import dp
from aiogram import types
from keyboards.inline import back_from_write_city_to_main_menu, to_main_menu_from_city
from weather_api import city
from states import PushButton
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


# Выбор погоды по названию города
@dp.callback_query_handler(text="back_to_write_city_name", state='*')
@dp.callback_query_handler(text="city_name_weather", state='*')
async def by_city_name_weather(call: CallbackQuery, state:FSMContext):

    await call.message.answer(text="Введи название города", reply_markup=to_main_menu_from_city)
    await PushButton.after_push_city_button.set()


# Выдача погоды по названию города
@dp.message_handler(content_types=['text'], state=PushButton.after_push_city_button)
async def answer_after_write_city_name(message: types.Message, state: FSMContext):
    try:
        text = city(city_name=message.text)
        await message.answer(text=text, reply_markup=back_from_write_city_to_main_menu)
        await state.finish()
    except Exception as exc:
        await message.answer(f'Не знаю такой город... '
                                     f'. Попробуй ввести новый населенный пункт',
                             reply_markup=back_from_write_city_to_main_menu)
