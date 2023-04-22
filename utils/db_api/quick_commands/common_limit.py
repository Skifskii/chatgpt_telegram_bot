from asyncpg import UniqueViolationError

from logs.log_all import log_all
from utils.db_api.schemas.common_limit import CommonLimit


async def set_common_limit(value: int):
    try:
        limits = await CommonLimit.query.gino.all()
        limit = limits[0]
        await limit.update(value=value).apply()
    except UniqueViolationError as error:
        await log_all('set_common_limit', 'error', '', '', f'Limit did not changed: {error}')


async def get_common_limit():
    limits = await CommonLimit.query.gino.all()
    limit = limits[0]
    return limit.value
