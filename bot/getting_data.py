import aiohttp
from aiogram import types
from .config import proxy, user, password


async def fetch(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                product_name = x['product_model']
                img = 'media/Снимок_экрана_1_eDZxo9U.png'
                with open(img, 'rb') as f:
                    cate = f.read()
                description = x['description']
                await message.answer_photo(cate)
                await message.answer(f'{product_name}'
                                     f'\n{description}'
                                     )

