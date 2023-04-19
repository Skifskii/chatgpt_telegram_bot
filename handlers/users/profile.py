from aiogram import types

from loader import dp
from utils.db_api.quick_commands import user as db_users

from data.texts import unknown_error_answer
from logs.log_all import log_all


@dp.message_handler(commands='profile')
async def command_profile(message: types.Message):
    try:
        user = await db_users.select_user(message.from_user.id)
        answer_text = f'👤 {user.firstname}\nСтатус: {user.status}'
        if user.max_limit >= 0:
            answer_text += f'\nДоступные запросы: {user.limit}/{user.max_limit}'
        await message.answer(answer_text)
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('profile', 'error', message.from_user.id, message.from_user.first_name, error)
