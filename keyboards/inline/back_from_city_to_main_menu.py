from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji


back_from_write_city_to_main_menu = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text= emoji.emojize(":leftwards_arrow_with_hook:", use_aliases=True) + "назад",
                callback_data="back_to_write_city_name"
            )
        ],
        [
            InlineKeyboardButton(
                text=emoji.emojize(":house:", use_aliases=True) + " меню",
                callback_data="from_city_to_main_menu"
            )
        ]
    ]
)

to_main_menu_from_city = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=emoji.emojize(":leftwards_arrow_with_hook:", use_aliases=True) + "назад",
                callback_data="back_from_city_to_main_menu"
            )
        ]
    ]
)