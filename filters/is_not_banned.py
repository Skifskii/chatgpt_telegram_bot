from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.texts import ban_answer, limit_answer
from utils.db_api.quick_commands import user as db_users


class IsNotBanned(BoundFilter):
    async def check(self, message: types.Message):
        try:
            user = await db_users.select_user(message.from_user.id)
            if user.status == 'ban':
                await message.answer(ban_answer)
                return False
            if user.status == 'user' and user.limit == 0:
                await message.answer(limit_answer)
                return False
            return True
        except AttributeError:
            return False
