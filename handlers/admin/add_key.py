from aiogram import types

from filters import IsAdmin
from loader import dp
from utils.db_api.quick_commands import openai_key as db_openai_key

from data.texts import unknown_error_answer
from logs.log_all import log_all


@dp.message_handler(IsAdmin(), commands='add_key')
async def add_key_command(message: types.Message):
    try:
        if 'sk-' not in message.get_args():
            await message.answer('Проверьте правильность введенного ключа.')
            return
        await db_openai_key.add_key(message.get_args())
        await message.answer('Ключ успешно добавлен!')
        await log_all('add_key_command', 'info', message.from_user.id, message.from_user.first_name, 'Key added')
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('start_stat', 'error', message.from_user.id, message.from_user.first_name, error)
