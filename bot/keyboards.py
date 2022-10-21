from aiogram import types
from .getting_data import buttons


def kb():
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
    return keyboard


def kb1():
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
    return keyboard


def kb2():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*buttons)
    keyboard.add(types.KeyboardButton(text="Go Back."))
    buttons.clear()

    return keyboard
