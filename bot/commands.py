from aiogram import types
from .control import dp
from .getting_data import fetch, key
from .keyboards import kb, kb1, kb2


@dp.message_handler(commands=["start"])
async def on_start(message: types.Message):
    await message.reply(
        text=f"Hi bot {message.from_user.full_name}",
        reply_markup=kb()
    )


@dp.message_handler(text='Продукция 📦')
async def choice_lang(message: types.Message):
    await message.answer(
        text="Выбрайте", reply_markup=kb1()
    )


@dp.message_handler(text='ВСТРАИВАЕМАЯ ТЕХНИКА')
async def choice_lang1(message: types.Message):
    await key()
    await message.answer(
        text="Выбрайте", reply_markup=kb2()
    )


@dp.message_handler(text='Go Back')
async def choice_lang1(message: types.Message):
    await message.answer(
        text="Выбрайте", reply_markup=kb()
    )


@dp.message_handler(content_types=types.ContentType.TEXT)
async def lang(message: types.Message):
    mes = message.text
    res = await fetch()
    for x in res:
        name = x['product_model']
        description = x['description']
        if mes == x['product_model']:
            await message.answer(f'{name}'
                                 f'\n{description}'
                                 )
    if mes == 'Go Back.':
        await message.answer(f'.', reply_markup=kb1())
