from aiogram import types
import logging_loguru

from loader import dp
from utils.db_api.quick_commands import user as db_users
from utils.db_api.quick_commands import stat as db_stat
from utils.db_api.quick_commands import telegram_log_permission as db_telegram_log_permission

from utils.notify_admins import notify_admins
from data.texts import start_answer
from logging_loguru.logger import logger

@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    try:
        user = await db_users.select_user(message.from_user.id)
        if not user:
            await db_users.add_user(user_id=message.from_user.id, name=message.from_user.first_name)
            await db_stat.add_new_user_to_stats()
            # logging_loguru.warning(f"Added new user! id: {message.from_user.id}; name: {message.from_user.first_name}")
            if (await db_telegram_log_permission.select_permissions())[0].new_users == 1:
                await notify_admins(dp, f"⚙👋 Added new user! id: {message.from_user.id}; name: {message.from_user.first_name}")
                # await bot.send_message(os.getenv("ADMINS_TELEGRAM_ID").split(',')[0],
                #                        f"⚙👋 Added new user! id: {message.from_user.id}; name: {message.from_user.first_name}")
    except Exception as error:
        # logging_loguru.exception(f"User id: {message.from_user.id}; name: {message.from_user.first_name} :: Error: {error}")
        if (await db_telegram_log_permission.select_permissions())[0].errors == 1:
            await notify_admins(f"⚙⚠ User id: {message.from_user.id}; name: {message.from_user.first_name} :: Error: {error}")
            # await bot.send_message(os.getenv("ADMINS_TELEGRAM_ID").split(',')[0],
            #                        f"⚙⚠ User id: {message.from_user.id}; name: {message.from_user.first_name} :: Error: {error}")
        await message.answer("Что-то пошло не так :(")
    logger.info('New user')
    await message.answer(start_answer.format(first_name=message.from_user.first_name))
