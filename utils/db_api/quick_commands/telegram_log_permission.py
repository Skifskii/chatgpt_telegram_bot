from asyncpg import UniqueViolationError

from utils.db_api.schemas.telegram_log_permission import TelegramLogPermission


async def add_row_to_tg_log_permissions():
    try:
        perms = TelegramLogPermission()
        await perms.create()
    except UniqueViolationError:
        print('Error in permissions')


async def select_permissions():
    perms = (await TelegramLogPermission.query.gino.all())
    return perms


async def reset_permissions(new_statuses):
    perms = (await TelegramLogPermission.query.gino.all())[0]
    await perms.update(messages=new_statuses[0], new_users=new_statuses[1], errors=new_statuses[2]).apply()
