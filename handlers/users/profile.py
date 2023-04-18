from aiogram import types

from loader import dp
from utils.db_api.quick_commands import user as db_users

from data.config import subscriptions_dict
from data.texts import profile_answer, unknown_error_answer
from logs.log_all import log_all


@dp.message_handler(commands='profile')
async def command_profile(message: types.Message):
    try:
        user = await db_users.select_user(message.from_user.id)
        user_subscription = subscriptions_dict[user.status]
        await message.answer(profile_answer.format(user_name=user.firstname, user_subscription=user_subscription))
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('profile', 'error', message.from_user.id, message.from_user.first_name, error)
