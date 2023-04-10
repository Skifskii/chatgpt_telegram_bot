import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = str(os.getenv('TELEGRAM_TOKEN'))
admins_id = [
    487799406
]
PG_HOST = str(os.getenv('PG_HOST'))
PG_USER = str(os.getenv('PG_USER'))
PG_PASSWORD = str(os.getenv('PG_PASSWORD'))
PG_DATABASE = str(os.getenv('PG_DATABASE'))
POSTGRES_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DATABASE}'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

subscriptions_dict = {
    'gpt': 'GPT',
    'dalle': 'DALL-E',
    'vip': 'VIP'
}
