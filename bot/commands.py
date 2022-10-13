from aiogram import types
from bot.control import dp
from bot.getting_data import fetch


@dp.message_handler(commands=["start"])
async def on_start(message: types.Message):
    await message.reply(
        text=f"Hi bot {message.from_user.full_name}"
    )


@dp.message_handler(commands="get")
async def ListOffTask(message: types.Message):
    await fetch(message)
