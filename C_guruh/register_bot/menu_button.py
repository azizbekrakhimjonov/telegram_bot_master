from aiogram.types import *

# register, data
register = KeyboardButton('Royhatdan o`tish')
data = KeyboardButton('Kurslar')
tel = KeyboardButton('PhoneNumber')

btn_start = ReplyKeyboardMarkup(resize_keyboard=True).add(register, data).add(tel)

# register buttons
python = KeyboardButton('Python')
java = KeyboardButton('Java')
web = KeyboardButton('Web')
grafik = KeyboardButton('Grafik dizayn')
arhitektura = KeyboardButton('Arhitektura va Dizayn')
robototehnika = KeyboardButton('Mobil Robototexnika')
bc = KeyboardButton('<--Back')
ks = KeyboardButton('KS')
english = KeyboardButton('It-english')
btn_register = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(python, java)\
    .add(web, grafik)\
    .add(arhitektura, robototehnika)\
    .add(ks, english)\
    .add(bc)

back = ReplyKeyboardMarkup(resize_keyboard=True).add()