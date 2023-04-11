from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('forget', 'Очистить память'),
        types.BotCommand('profile', 'Профиль')
    ])
