from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.utils.markdown import hbold
from keyboards.inline import greeting_inline_menu
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


# Стартовое приветствие
@dp.message_handler(Command("start"), state='*')
async def start_greeting(message: types.Message, state: FSMContext):
    await message.answer('Привет ' + hbold(f'{message.chat.first_name}') + ', я погодный бот. \n\n'
                         + 'Если тебе нужно узнать погоду - я тебе помогу\n\n'
                           'Просто выбери, что тебе нужно: ', reply_markup=greeting_inline_menu)
    await state.finish()


@dp.callback_query_handler(text="from_2_branchline_to_main_menu", state='*')
@dp.callback_query_handler(text="now_from_3_to_main_menu", state='*')
@dp.callback_query_handler(text='go_to_main_menu', state='*')
@dp.callback_query_handler(text="from_city_to_main_menu", state='*')
@dp.callback_query_handler(text="back_from_city_to_main_menu", state="*")
@dp.callback_query_handler(text="main_menu", state="*")
async def press_menu_button(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text='Привет ' + hbold(f'{call.message.chat.first_name}') + ', я погодный бот. \n\n'
                         + 'Если тебе нужно узнать погоду - я тебе помогу\n\n'
                          'Просто выбери, что тебе нужно: ', reply_markup=greeting_inline_menu)

    await state.finish()

# TODO Добавить модуль смены языка (реализовать через состояние)
# TODO Возможность администрирования бота через анминскую кансоль - через пароль лого, смена тайтла, дискрипшина и т.д.)
# TODO Сделать округление температуры до целых чисел