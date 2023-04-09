from logs.logging_loguru.logger import logger
from utils.notify_admins import notify_admins
from loader import dp
from utils.db_api.quick_commands import telegram_log_permission as db_telegram_log_permission


async def log_all(func_name, level, user_id='', user_name='', log_message=''):
    emoji = ''
    if level == 'info':
        emoji = '⚙ℹ Info'
        logger.info(f"in {func_name} :: id: {user_id}, name: {user_name} :: {log_message}")
    if level == 'warning':
        emoji = '⚙⚠ Warning'
        logger.warning(f"in {func_name} :: id: {user_id}, name: {user_name} :: {log_message}")
    if level == 'error':
        emoji = '⚙🚫 Error'
        logger.warning(f"in {func_name} :: id: {user_id}, name: {user_name} :: {log_message}")
    await notify_admins(dp, f'{emoji}\nin {func_name} :: id: {user_id}, name: {user_name} :: {log_message}')
