from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# register & info
register = KeyboardButton('register')
info = KeyboardButton('kurslar')
menu_1 = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(register, info)
