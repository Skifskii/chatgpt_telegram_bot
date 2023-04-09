from aiogram import types

from loader import dp

from data.texts import help_answer
from logs.log_all import log_all


@dp.message_handler(commands='help')
async def command_help(message: types.Message):
    try:
        await message.answer(help_answer)
    except Exception as error:
        await message.answer('Что-то пошло не так :(')
        await log_all('start', 'error', message.from_user.id, message.from_user.first_name, error)
