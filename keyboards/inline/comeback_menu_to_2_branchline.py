from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji

comeback_to_2_branchline = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
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