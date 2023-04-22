from asyncpg import UniqueViolationError

from logs.log_all import log_all
from utils.db_api.schemas.openai_key import OpenaiKey


async def add_key(key: str):
    try:
        new_key = OpenaiKey(key=key)
        await new_key.create()
    except UniqueViolationError as error:
        await log_all('add_key', 'error', '', '', f'Key did not added: {error}')


async def get_key():
    key = await OpenaiKey.query.where(OpenaiKey.status == 'using').gino.first()
    return key.key


async def reset_key():
    await OpenaiKey.delete.where(OpenaiKey.status == 'using').gino.status()
    key = await OpenaiKey.query.where(OpenaiKey.status == 'waiting').gino.first()
    await key.update(status='using').apply()
    return key.key
