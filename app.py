async def on_startup_app(dp):
    from loader import db
    from utils.db_api.db_gino import on_startup_db
    await on_startup_db(dp)
    await db.gino.create_all()

    from utils.notify_admins import notify_admins

    await notify_admins(dp, 'Bot started')

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    print('Bot started')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup_app)
