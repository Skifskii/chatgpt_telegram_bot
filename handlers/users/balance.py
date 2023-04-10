from aiogram import types

from keyboards.inline import ikb_buy
from loader import dp
from utils.db_api.quick_commands import user as db_users

from data.texts import balance_answer
from logs.log_all import log_all


@dp.message_handler(commands='balance')  # ToDo
async def command_balance(message: types.Message):
    try:
        user = await db_users.select_user(message.from_user.id)
        await message.answer(balance_answer.format(user_balance=user.balance, english_words=int(user.balance * 0.7)), reply_markup=ikb_buy)
    except Exception as error:
        await message.answer('Что-то пошло не так :(')
        await log_all('balance', 'error', message.from_user.id, message.from_user.first_name, error)
