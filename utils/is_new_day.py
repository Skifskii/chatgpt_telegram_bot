import asyncio
from datetime import date

from logs.log_all import log_all
from utils.db_api.quick_commands import stat as db_stat
from utils.db_api.quick_commands import user as db_users


async def set_new_day():
    print('hi')
    await db_stat.reset_stat(str(date.today()))
    users = await db_users.select_all_users()
    for user in users:
        await db_users.reset_limit(user.user_id, user.max_limit)
    await log_all('set_new_day', 'info', '', '', 'Лимиты пользователей обновлены')
