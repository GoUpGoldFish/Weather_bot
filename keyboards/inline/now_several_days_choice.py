from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji


now_several_days_choice = InlineKeyboardMarkup(row_width=2,
                                               inline_keyboard=[
                                                   [
                                                       InlineKeyboardButton(
                                                           text="сейчас",
                                                           callback_data="now"
                                                       ),
                                                       InlineKeyboardButton(
                                                           text="на несколько дней",
                                                           callback_data="for_several_days"
                                                       )
                                                   ],
                                                   [
                                                       InlineKeyboardButton(
                                                           text=emoji.emojize(":leftwards_arrow_with_hook:", use_aliases=True) + "назад",
                                                           callback_data="back_to_main_menu"
                                                       )
                                                   ]
                                               ])