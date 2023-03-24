import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = str(os.getenv("TELEGRAM_TOKEN"))
admins_id = [
    487799406
]
