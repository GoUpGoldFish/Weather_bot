from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

send_geolocation = ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=True,
                                       keyboard=[
                                 [
                                     KeyboardButton(
                                         text=emoji.emojize(":globe_with_meridians:", use_aliases=True) + ' отправить'
                                                                                                          ' геолокацию',
                                         request_location=True
                                     )
                                 ],
                                 # [
                                 #     KeyboardButton(
                                 #         text=emoji.emojize(":house:", use_aliases=True) + " меню"
                                 #     )
                                 # ]

                             ])
