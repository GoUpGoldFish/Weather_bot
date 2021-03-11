from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji

greeting_inline_menu = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=emoji.emojize(":earth_americas:", use_aliases=True) + "Погода по геолокации",
                callback_data="geolocation_weather"
            )
        ],
        [
            InlineKeyboardButton(
                text=emoji.emojize(":black_nib:", use_aliases=True) + "Погода по названию города",
                callback_data="city_name_weather"
            )
        ]
    ])
