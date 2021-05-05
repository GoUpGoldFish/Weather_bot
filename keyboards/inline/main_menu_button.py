from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

main_menu_button = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=emoji.emojize(":house:", use_aliases=True) + " меню",
                callback_data="main_menu"
            )
        ]
    ]
)
