from aiogram import Dispatcher

from .is_admin import IsAdmin
from .is_not_banned import IsNotBanned


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsNotBanned)
