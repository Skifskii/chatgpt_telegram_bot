from aiogram import types

from loader import dp
from utils.db_api.quick_commands import user as db_users
from utils.db_api.quick_commands import stat as db_stat

from data.texts import start_answer, unknown_error_answer
from logs.log_all import log_all


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    try:
        user = await db_users.select_user(message.from_user.id)
        if not user:
            await db_users.add_user(user_id=message.from_user.id, username=message.from_user.username, name=message.from_user.first_name)
            await db_stat.add_new_user_to_stats()
            await log_all('start', 'info', message.from_user.id, message.from_user.first_name, 'New user')
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('start', 'error', message.from_user.id, message.from_user.first_name, error)
    await message.answer(start_answer.format(first_name=message.from_user.first_name))
