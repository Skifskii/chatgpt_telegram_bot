from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_subscribe = InlineKeyboardMarkup()

btn_subscribe_gpt = InlineKeyboardButton(text='GPT', callback_data='btn_subscribe_gpt')
ikb_subscribe.insert(btn_subscribe_gpt)

btn_subscribe_dalle = InlineKeyboardButton(text='DALL-E', callback_data='btn_subscribe_dalle')
ikb_subscribe.insert(btn_subscribe_dalle)

btn_subscribe_vip = InlineKeyboardButton(text='VIP', callback_data='btn_subscribe_vip')
ikb_subscribe.insert(btn_subscribe_vip)
