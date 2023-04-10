from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_buy = InlineKeyboardMarkup()

btn_buy = InlineKeyboardButton(text='Пополнить', callback_data='btn_buy')
ikb_buy.insert(btn_buy)
