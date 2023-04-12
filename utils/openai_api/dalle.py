import openai


async def request_to_dalle(new_prompt: str, new_size: str) -> str:
    response = openai.Image.create(
        prompt=new_prompt,
        n=1,
        size=new_size
    )
    return response['data'][0]['url']
