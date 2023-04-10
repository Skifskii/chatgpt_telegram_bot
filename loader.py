import openai
from aiogram import Bot, types, Dispatcher

from utils.db_api.db_gino import db
from data import config

openai.api_key = config.OPENAI_API_KEY
bot = Bot(token=config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

__all__ = ['bot', 'dp', 'db']
