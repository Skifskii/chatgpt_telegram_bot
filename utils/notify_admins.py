from aiogram import Dispatcher
from logs.logging_loguru.logger import logger
from utils.db_api.quick_commands import user as db_users
from utils.db_api.quick_commands import telegram_log_permission as db_tg_logs


async def notify_admins(dp: Dispatcher, text: str, level):
    try:
        users = await db_users.select_all_users()
        for user in users:
            if user.status == 'admin':
                perms = await db_tg_logs.select_admin_permissions(user.user_id)
                if perms[level]:
                    await dp.bot.send_message(chat_id=user.user_id, text=text)
    except Exception as error:
        logger.error(f'in notify_admins :: {error}')
