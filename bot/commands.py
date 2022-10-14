from aiogram import types
from .control import dp
from .getting_data import fetch


@dp.message_handler(commands=["start"])
async def on_start(message: types.Message):
    await message.reply(
        text=f"Hi bot {message.from_user.full_name}"
    )
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["Uzb", "Rus"]
    keyboard.add(*buttons)
    await message.answer(
        text=f"Xush kelibsz {message.from_user.full_name}",
        reply_markup=keyboard
    )


@dp.message_handler(content_types=types.ContentType.TEXT)
async def choice_lang(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Продукция 📦"),
        types.KeyboardButton(text="Контакты 📩"),
        types.KeyboardButton(text="О нас 💬"),
        types.KeyboardButton(text="Почему мы ⁉"),
        types.KeyboardButton(text="Наши магазины 🏪"),
        types.KeyboardButton(text="Новости 📝"),
        types.KeyboardButton(text="Наши сервисные центры ⚙"),
        types.KeyboardButton(text="Онлайн каталог 📓")
            )
    language = message.text.title()
    if language == "Rus":
        "Вы набрали руский язык"
        await message.answer(
            text="Выбрайте",
            reply_markup=keyboard
        )


@dp.message_handler(commands="get")
async def ListOffTask(message: types.Message):
    await fetch(message)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def choice_lang1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="ВСТРАИВАЕМАЯ ТЕХНИКА"),
        types.KeyboardButton(text="ВАРОЧНЫЙ ЦЕНТР"),
        types.KeyboardButton(text="КОНДИЦИОНЕРЫ"),
        types.KeyboardButton(text="ПОСУДОМОЕЧНЫЕ МАШИНЫ"),
        types.KeyboardButton(text="МИКРОВОЛНОВЫЕ ПЕЧИ"),
        types.KeyboardButton(text="ПЫЛЕСОС"),
        types.KeyboardButton(text="ХОЛОДИЛЬНИКИ"),
        types.KeyboardButton(text="Go Back")
    )
    language = message.text.title()
    if language == "Продукция 📦":
        await message.reply(f'', reply_markup=types.ReplyKeyboardRemove())
        await message.answer(f' Вибрайте:', reply_markup=keyboard)


