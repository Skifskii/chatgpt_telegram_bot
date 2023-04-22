from aiogram import types

from filters import IsAdmin
from loader import dp
from utils.db_api.quick_commands import common_limit as db_common_limit
from utils.db_api.quick_commands import user as db_user

from data.texts import unknown_error_answer
from logs.log_all import log_all


@dp.message_handler(IsAdmin(), commands='change_common_limit')
async def change_common_limit(message: types.Message):
    try:
        new_limit = int(message.get_args())
        await db_common_limit.set_common_limit(new_limit)
        users = await db_user.select_all_users()
        for user in users:
            await db_user.reset_max_limit(user.user_id, new_limit)
            await db_user.reset_limit(user.user_id, new_limit)
        await message.answer('Лимит изменен для всех пользователей!')
        await log_all('change_common_limit', 'info', message.from_user.id, message.from_user.first_name, 'Common limit changed')
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('change_common_limit', 'error', message.from_user.id, message.from_user.first_name, error)
