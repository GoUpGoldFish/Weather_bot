from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

html_string = '\n'.join(
    [
        'Привет, ' + hbold('Виталик!'),
        'Как говорится:',
        hitalic('Боятся надо не смерти, а пустой жизни.'),
        '',
        'Но мы сейчас не об этом. ' + hstrikethrough('Что тебе нужно?'),
        'Этот текст с html форматированием. '
        'Почитать об этом можно ' + hlink('тут',
                                          'https://core.telegram.org/bots/api#formatting-options'),
        hunderline('Внимательно прочти и используй с умом!'),
        '',
        hcode('Пример использования - ниже:'),
        '',
        '']
)
html_string += hcode(html_string)


@dp.message_handler(Command('parse_mode_html'))
async def show_parse_mode(message: types.Message):
    await message.answer(html_string)