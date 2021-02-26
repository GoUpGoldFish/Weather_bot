from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback


choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Купить грушу",
                                          callback_data=buy_callback.new(item_name='pear',
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text='Купить яблоки',
                                          callback_data=buy_callback.new(item_name='apple',
                                                                         quantity=5)
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data='cancel'
                                      )
                                  ]
                              ])

pear_keyboard = InlineKeyboardMarkup()
PEAR_LINK = 'https://russian.alibaba.com/product-detail/fresh-yellow-pear-for-sale-fresh-fruits-pears-quality-pears' \
            '-1600139331994.html?spm=a2700.7724857.normal_offer.d_image.4ee33dc2U1p59n'
pear_link = InlineKeyboardButton(text='Купи тут', url=PEAR_LINK)
pear_keyboard.insert(pear_link)

apple_keyboard = InlineKeyboardMarkup()
APPLE_LINK = 'https://russian.alibaba.com/product-detail/china-apple-the-lowest-price-fresh-fuji-apple-607231125' \
             '87.html?spm=a2700.galleryofferlist.topad_classic.d_image.486537caZwl6ww'
apple_link = InlineKeyboardButton(text='Купи тут', url=APPLE_LINK)
apple_keyboard.insert(apple_link)