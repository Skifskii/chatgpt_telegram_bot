from asyncpg import UniqueViolationError

from logs.log_all import log_all
from utils.db_api.schemas.user import User


# ---------- User ----------
async def add_user(user_id: int, username: str, name: str):
    try:
        user = User(user_id=user_id, name=name, username=username)
        await user.create()
    except UniqueViolationError as error:
        await log_all(add_user, error, user_id, name, f'User did not added: {error}')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def add_story(user_id, messages):
    user = await select_user(user_id)
    await user.update(chat_story=messages).apply()


async def get_story(user_id):
    user = await select_user(user_id)
    return user.chat_story


async def set_email(user_id, email):
    user = await select_user(user_id)
    await user.update(email=email).apply()


async def get_email(user_id):
    user = await select_user(user_id)
    return user.email


async def clear_story(user_id):
    user = await select_user(user_id)
    await user.update(chat_story='{"messages":[]}').apply()


async def set_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def commit_new_message(user_id):
    user = await select_user(user_id)
    await user.update(total_messages_sent=user.total_messages_sent + 1).apply()


async def commit_new_image(user_id):
    user = await select_user(user_id)
    await user.update(total_images_generated=user.total_images_generated + 1).apply()


async def set_user_status_for_all():
    users = await select_all_users()
    for user in users:
        await user.update(status='user', total_images_generated=0, total_messages_sent=0).apply()
