from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

img = KeyboardButton('image')
mp3 = KeyboardButton('audio')
mp4 = KeyboardButton('video')
xls = KeyboardButton('excel')
txt = KeyboardButton('text')
menu_button = ReplyKeyboardMarkup(resize_keyboard=True).add(img, mp3).add(xls,txt).add(mp4)
