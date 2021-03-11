from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

choice = ReplyKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             keyboard=[
                                 [
                                     KeyboardButton(
                                         text=emoji.emojize(":globe_with_meridians:", use_aliases=True) + ' отправить'
                                                                                                          ' геолоккацию',
                                         request_location=True
                                     )],
                                 [
                                     KeyboardButton(
                                         text=emoji.emojize(":wrench:", use_aliases=True) + ' меню'
                                     )
                                 ]
                             ])
