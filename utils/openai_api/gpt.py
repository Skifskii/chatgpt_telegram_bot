import openai

from data import config
from utils.db_api.quick_commands import openai_key as db_openai_key

async def request_to_gpt(request: dict) -> tuple[str, int]:
    response = await openai.ChatCompletion.acreate(
        model='gpt-3.5-turbo',
        messages=request,
        api_key=await db_openai_key.get_key()
    )
    return response['choices'][0]['message']['content'], response['usage']['total_tokens']
