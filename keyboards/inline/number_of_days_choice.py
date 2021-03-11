from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji


number_of_days_choice = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text=emoji.emojize(":one:", use_aliases=True),
                                                         callback_data="1_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text=emoji.emojize(":two:", use_aliases=True),
                                                         callback_data="2_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text=emoji.emojize(":three:", use_aliases=True),
                                                         callback_data="3_number_of_days"
                                                     ),
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text=emoji.emojize(":four:", use_aliases=True),
                                                         callback_data="4_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text=emoji.emojize(":five:", use_aliases=True),
                                                         callback_data="5_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text=emoji.emojize(":six:", use_aliases=True),
                                                         callback_data="6_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text=emoji.emojize(":seven:", use_aliases=True),
                                                         callback_data="7_number_of_days"
                                                     ),
                                                 ]

                                             ])