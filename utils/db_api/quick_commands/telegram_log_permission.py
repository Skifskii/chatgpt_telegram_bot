from asyncpg import UniqueViolationError

from utils.db_api.schemas.telegram_log_permission import TelegramLogPermission
from logs.logging_loguru.logger import logger

async def add_admin(admin_id):
    try:
        perms = TelegramLogPermission(admin_id=admin_id)
        await perms.create()
    except UniqueViolationError as error:
        logger.error(f"in add_admin :: {error}")


async def select_admin_permissions(admin_id):
    try:
        perms = await TelegramLogPermission.query.where(TelegramLogPermission.admin_id == admin_id).gino.first()
        return {'info': perms.info, 'warning': perms.warning, 'error': perms.error}
    except AttributeError:
        await add_admin(admin_id)
        return {'info': 1, 'warning': 1, 'error': 1}


async def reset_permissions(new_statuses, admin_id):
    perms = await TelegramLogPermission.query.where(TelegramLogPermission.admin_id == admin_id).gino.first()
    await perms.update(info=new_statuses[0], warning=new_statuses[1], error=new_statuses[2]).apply()
