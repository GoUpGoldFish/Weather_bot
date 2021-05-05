from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji


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
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                          text=emoji.emojize(":leftwards_arrow_with_hook:",
                                                                                    use_aliases=True) + "назад",
                                                          callback_data="now_from_3_to_2_branchline"
                                                      )
                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                          text=emoji.emojize(":house:", use_aliases=True) + ' меню',
                                                          callback_data="now_from_3_to_main_menu"
                                                      )
                                                 ]

                                             ])

