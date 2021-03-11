from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


number_of_days_choice = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text="1",
                                                         callback_data="1_number_of_days",
                                                     ),
                                                     InlineKeyboardButton(
                                                         text="2",
                                                         callback_data="2_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text="3",
                                                         callback_data="3_number_of_days"
                                                     ),
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text="4",
                                                         callback_data="4_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text="5",
                                                         callback_data="5_number_of_days"
                                                     ),
                                                     InlineKeyboardButton(
                                                         text="6",
                                                         callback_data="6_number_of_days"
                                                     ),
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text="7",
                                                         callback_data="7_number_of_days"
                                                     ),
                                                 ]

                                             ])

