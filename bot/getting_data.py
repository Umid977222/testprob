import aiohttp
from aiogram import types
from bot.config import proxy, user, password


async def fetch(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(proxy, auth=aiohttp.BasicAuth(user, password)) as response:
            data = await response.json()
            for x in data:
                product_name = x['product_model']
                img = x['img']
                # with open(img, 'rb') as f:
                #     cate = f.read()
                description = x['description']
                await message.answer_photo(img)
                await message.answer(f'{product_name}'
                                     f'\n{description}'
                                     )

