import asyncio
from datetime import date

from logs.log_all import log_all
from utils.db_api.quick_commands import stat as db_stat
from utils.db_api.quick_commands import user as db_users


async def is_new_day():
    while True:
        await asyncio.sleep(60)
        stat = await db_stat.take_stat()
        if str(date.today()) > stat.date_today:
            await db_stat.reset_stat(str(date.today()))
            users = await db_users.select_all_users()
            for user in users:
                await db_users.reset_limit(user.user_id, user.max_limit)
            await log_all('is_new_day' 'info', '', '', 'Лимиты пользователей обновлены')
