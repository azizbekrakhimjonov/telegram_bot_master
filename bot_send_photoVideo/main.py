import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

from config import token
from buttons import *
logging.basicConfig(level=logging.INFO)


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=menu_button)



@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'image':
        URL = 'https://www.meme-arsenal.com/memes/e0f221253de3a3d2282072561453b45f.jpg'
        await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))
    if message.text == 'audio':
        audio = InputFile("gioPika.mp3")
        await bot.send_audio(chat_id=message.chat.id, audio=audio)
    if message.text == 'video':
        video = open("py.mp4", "rb")
        await bot.send_video(message.chat.id, video=video)
    if message.text == 'excel':
        excel = open("mySelf.xlsx", "rb")
        await bot.send_document(message.chat.id, document=excel)
    if message.text == 'text':
        txt = open("SQL_methods.txt", "rb")
        await bot.send_document(message.chat.id, document=txt)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)