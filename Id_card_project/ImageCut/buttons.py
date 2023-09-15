from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_result = KeyboardButton('Получить ID карту')
button_start = KeyboardButton('Назад')
button_cansel = KeyboardButton('Отменить заявку')
result = ReplyKeyboardMarkup(resize_keyboard=True).add(button_result)
start_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_start)
cansel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cansel)