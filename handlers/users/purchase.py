from aiogram.types import CallbackQuery, ReplyKeyboardRemove
import logging
from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apple_keyboard
from loader import dp, bot
from aiogram.dispatcher.filters import Command
from aiogram import types


@dp.message_handler(Command("items"))
async def show_inline_keyboard(message: types.Message):
    await message.answer(text="На продажу у нас есть 2 товара:"
                              " 5 яблок и 1 груша.\n"
                              "Если вам ничего не нужно - жмите отмену",
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name='pear'))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали купить грушу. Груш всего {quantity}. Спасибо.',
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_apple(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали купить яблоки. Яблок всего {quantity}. Спасибо.',
                              reply_markup=apple_keyboard)


@dp.callback_query_handler(text='cancel')
async def push_cancel(call: CallbackQuery):
    await call.answer('Вы отменили там что то...', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
