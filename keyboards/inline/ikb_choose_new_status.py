from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_choose_new_status = InlineKeyboardMarkup(row_width=2)

btn_status_gpt = InlineKeyboardButton(text='Безлимит', callback_data='btn_status_unlimited')
ikb_choose_new_status.insert(btn_status_gpt)

btn_status_vip = InlineKeyboardButton(text='Изменить лимит', callback_data='btn_status_limited')
ikb_choose_new_status.insert(btn_status_vip)

btn_status_user = InlineKeyboardButton(text='Заблокировать', callback_data='btn_status_ban')
ikb_choose_new_status.insert(btn_status_user)

btn_status_admin = InlineKeyboardButton(text='Разблокировать', callback_data='btn_status_unban')
ikb_choose_new_status.insert(btn_status_admin)

btn_status_ban = InlineKeyboardButton(text='admin', callback_data='btn_status_admin')
ikb_choose_new_status.insert(btn_status_ban)

btn_back = InlineKeyboardButton(text='🔙 Отмена', callback_data='btn_back')
ikb_choose_new_status.insert(btn_back)
