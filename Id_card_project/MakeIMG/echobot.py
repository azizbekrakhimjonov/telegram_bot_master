import logging

from aiofiles import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = "6384532641:AAF0e8iMw_ZNb1HGqkr8Kz3-X5KsRPyCgTQ"


logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message.from_user.id)
    await message.reply("upload photo")

# @dp.message_handler(content_types="photo")
# async def get_photo(message: types.Message):
#     # await message.photo[0].download(destination_file="photo1.jpg", make_dirs=False)
#     await message.photo[-1].download(destination_file='123.jpg', make_dirs=False)


@dp.message_handler(regexp='(^save[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Cats is here 😺',
                             reply_to_message_id=message.message_id)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)
    await bot.send_document(chat_id=message.chat.id, document=(f'user.pdf', 'r'))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)








# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('data/cats.jpg', 'rb') as photo:
#         await bot.send_photo(message.chat.id, photo, caption='Cats is here 😺',
#                              reply_to_message_id=message.message_id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)