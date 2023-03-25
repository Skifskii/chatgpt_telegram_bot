from aiogram import Dispatcher
from data.config import admins_id


async def notify_admins(dp: Dispatcher, text: str):
    for admin in admins_id:
        try:
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as error:
            print(error)
