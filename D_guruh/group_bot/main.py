import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InputFile

from config import token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)



# _________________kilent chat_______________________
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

    await message.reply("Assalomu aleykum botga xush kelibsiz!\nBotni qayta ishga tushurish uchun: /start\nrasim uchun: /img\nvideo uchun: /video\naudio uchun: /audio")

# _________________group chat_______________________
@dp.message_handler(commands=['img'])
async def send_img(message: types.Message):
    photo = InputFile('FOREST.png')
    await message.bot.send_photo(chat_id=message.chat.id, photo=photo)
    print(message.from_user.first_name)

@dp.message_handler(commands=['txt'])
async def send_img(message: types.Message):
    txt = InputFile('bot_send.txt')
    await message.bot.send_document(chat_id=message.chat.id, document=txt)
    print(message.from_user.first_name)


@dp.message_handler(commands=['video'])
async def send_video(message: types.Message):
    vid = open('py.mp4', 'rb')
    await message.bot.send_video(chat_id=message.chat.id, video=vid)

@dp.message_handler(commands=['audio'])
async def send_audio(message: types.Message):
    muz = open('gioPika.mp3', 'rb')
    await message.bot.send_audio(chat_id=message.chat.id, audio=muz)

@dp.message_handler()
async def get_img(message: types.Message):
    now = datetime.now()

    print(f'{now.hour}:{now.minute}:{now.second}-> {message.from_user.first_name}: {message.text}')
    # await bot.send_message(message.from_user.id, message.text)
    # if 'https://' in message.text:
    #     await message.answer('Reklama tarqatish mumkin emas!')
    #     await message.delete()
    # else:
    #     # await message.reply(f'Qoyil! {message.from_user.first_name}')
    #     await message.delete()



@dp.message_handler(content_types="photo")
async def get_img(message):
           await message.answer('Reklama tarqatish mumkin emas!')
           await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)

