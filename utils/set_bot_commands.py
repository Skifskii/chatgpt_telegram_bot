from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Начать общение'),
        types.BotCommand('help', 'О командах'),
        types.BotCommand('about', 'О боте'),
        types.BotCommand('forget', 'Очистить память'),
        types.BotCommand('profile', 'Профиль')
    ])
