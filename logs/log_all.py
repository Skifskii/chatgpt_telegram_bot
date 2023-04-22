from logs.logging_loguru.logger import logger
from utils.notify_admins import notify_admins
from loader import dp
from utils.db_api.quick_commands import telegram_log_permission as db_tgperms


async def log_all(func_name, level, user_id='', firstname='', log_message=''):
    try:
        if level == 'info':
            logger.info(f"in {func_name} :: id: {user_id}, firstname: {firstname} :: {log_message}")
            await notify_admins(dp,
                                f'⚙ℹ `Info`\nin `{func_name}` :: id: `{user_id}`, firstname: `{firstname}` :: `{log_message}`',
                                level)
        if level == 'warning':
            logger.warning(f"in {func_name} :: id: {user_id}, firstname: {firstname} :: {log_message}")
            await notify_admins(dp,
                                f'⚙⚠ `Warning`\nin `{func_name}` :: id: `{user_id}`, firstname: `{firstname}` :: `{log_message}`',
                                level)
        if level == 'error':
            logger.error(f"in {func_name} :: id: {user_id}, firstname: {firstname} :: {log_message}")
            await notify_admins(dp,
                                f'⚙🚫 `Error`\nin `{func_name}` :: id: `{user_id}`, firstname: `{firstname}` :: `{log_message}`',
                                level)
    except Exception as error:
        logger.error(f"in {log_all} :: id: {user_id}, firstname: {firstname} :: {error}")
