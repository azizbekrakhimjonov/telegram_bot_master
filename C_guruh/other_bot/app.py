import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from C_guruh.other_bot.config import token
logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Assalomu aleykum botga  hush kelibsiz\nvideo uchun: /video\naudio uchun: /audio\nrasm uchun: /img\ntxt uchun: /txt\nExcel uchun: /excel")

@dp.message_handler(commands=['img'])
async def send_img(message: types.Message):
    photo = InputFile("FOREST.png")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message_handler(commands=['audio'])
async def send_audio(message: types.Message):
    mp3 = InputFile("gioPika.mp3")
    await bot.send_audio(chat_id=message.chat.id, audio=mp3)

@dp.message_handler(commands=["video"])
async def send_video(message: types.Message):
    video = open("py.mp4", "rb")
    await bot.send_video(message.chat.id, video=video)

@dp.message_handler(commands=['excel'])
async def send_excel(message: types.Message):
    await bot.send_document(chat_id=message.chat.id, document=('mySelf.xlsx','r'))

@dp.message_handler(commands=['txt'])
async def send_txt(message: types.Message):
    await bot.send_document(chat_id=message.chat.id, document=('SQL_methods.txt','r'))



URL = 'https://www.meme-arsenal.com/memes/e0f221253de3a3d2282072561453b45f.jpg'
@dp.message_handler()
async def send_image(message: types.Message):
    await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))







if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)