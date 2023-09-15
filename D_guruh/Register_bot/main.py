import logging
from aiogram import Bot, Dispatcher, executor, types

from buttons import menu_1
from config import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum NI0TS obtga xush kelibsiz!",
                        reply_markup=menu_1)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text=='register':
        await message.answer('fullname: ')
    elif message.text=='kurslar':
        await message.answer('kurslar')
    else:
        await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)