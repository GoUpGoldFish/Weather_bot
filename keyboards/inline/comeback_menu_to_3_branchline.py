from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji


comeback_to_3_branchline = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=emoji.emojize(":leftwards_arrow_with_hook:",
                                                                                    use_aliases=True) + "назад",
                                                            callback_data="go_to_3_branchline"
                                                        )
                                                    ],
                                                    [
                                                        InlineKeyboardButton(
                                                            text=emoji.emojize(":house:", use_aliases=True) + ' меню',
                                                            callback_data="go_to_main_menu"
                                                        )
                                                    ]
                                                ])
