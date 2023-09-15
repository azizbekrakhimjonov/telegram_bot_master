# pip install pipenv
# pip install aiogram

import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

from D_guruh.config import token

logging.basicConfig(level=logging.INFO)


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Assalomu aleykum Botga hush kelibsiz!")

@dp.message_handler()
async def echo(message: types.Message):
    try:
        await message.answer(wikipedia.summary(message.text))
    except:
        await message.reply('Bunday maqola topilmadi!')
    # s = ['salom', 'hello', 'hi', 'Assalomu aleykum']
    # if message.text in s:
    #     getText = 'Vaaleykum assalom'
    # else:
    #     getText = message.text.upper()
    # await message.answer(getText)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)