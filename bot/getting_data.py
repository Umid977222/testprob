import aiohttp
from .config import url, user, password
buttons = []


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=aiohttp.BasicAuth(user, password)) as response:
            return await response.json()


async def key():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                product_name = x['product_model']
                if x['add_bot_button']:
                    buttons.append(product_name)
