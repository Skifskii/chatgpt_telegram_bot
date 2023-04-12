from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_change_user_status = InlineKeyboardMarkup()

btn_back = InlineKeyboardButton(text='🔙 Отмена', callback_data='btn_back')
ikb_change_user_status.insert(btn_back)

btn_change_status = InlineKeyboardButton(text='Изменить статус', callback_data='btn_change_status')
ikb_change_user_status.insert(btn_change_status)
