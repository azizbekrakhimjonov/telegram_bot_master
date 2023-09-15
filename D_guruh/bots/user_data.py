# pip install pipenv
# pip install aiogram

import logging
from aiogram import Bot, Dispatcher, executor, types
from D_guruh.config import token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

users = set()
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global users
    users.add(message.from_user.first_name)


@dp.message_handler(commands=["about"])
async def send_welcome(message: types.Message):
    await message.answer(f"Foydalanuvchilar soni: {len(users)}")

@dp.message_handler()
async def echo(message: types.Message):
    print(message.from_user.username)
    await message.answer('rahmaaat!\n😂😂😂😒😒')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)