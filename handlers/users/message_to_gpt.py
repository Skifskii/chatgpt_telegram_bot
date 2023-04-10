import json

import openai
from aiogram import types
from aiogram.types import ChatActions

from loader import dp, bot
from utils.db_api.quick_commands import user as db_users
from utils.db_api.quick_commands import stat as db_stat

from logs.log_all import log_all

@dp.message_handler()
async def send(message: types.Message):
    try:
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        user = await db_users.select_user(message.from_user.id)
        await db_stat.add_new_request_to_stats()
        messages = json.loads(await db_users.get_story(message.from_user.id))
        messages['messages'].append({"role": "user", "content": message.text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages['messages']
        )
        await message.answer(response["choices"][0]["message"]["content"])
        messages['messages'].append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})

        def replace_bsn_from_start(s):
            while s.startswith('\n'):
                s = s[1:]
            return s

        await db_stat.add_new_answer_to_stats()
        await db_stat.add_new_tokens_to_stats(response["usage"]["total_tokens"])
        await log_all('message_to_gpt', 'info', message.from_user.id, message.from_user.first_name, f'\n--------------------\nMessage:\n{message.text}\n\nAnswer:\n{replace_bsn_from_start(response["choices"][0]["message"]["content"])}\n--------------------')
    except Exception as error:
        await log_all('message_to_gpt', 'error', message.from_user.id, message.from_user.first_name, error)
