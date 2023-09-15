import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

token = '5300781695:AAEKQ9y5kg67h2JOe87WRNNvmy2fuRj_m64'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum botga xush kelibsiz!\nBotni qayta ishga tushurish uchun: /start\nrasim uchun: /img\nvideo uchun: /video\naudio uchun: /audio")

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
    # url = 'https://59d0-185-208-176-159.ngrok.io/m.mp4'
    # await message.bot.send_video(chat_id=message.chat.id,
    #                              video=types.InputFile.from_url(url))
    vid = open('py.mp4', 'rb')
    await message.bot.send_video(chat_id=message.chat.id, video=vid)

@dp.message_handler(commands=['audio'])
async def send_audio(message: types.Message):
    muz = open('gioPika.mp3', 'rb')
    await message.bot.send_audio(chat_id=message.chat.id, audio=muz)
    # url = 'https://59d0-185-208-176-159.ngrok.io/m.mp3'
    # await message.bot.send_audio(chat_id=message.chat.id,
    #                              audio=types.InputFile.from_url(url))



@dp.message_handler()
async def get_img(message: types.Message):

     url = 'https://www.meme-arsenal.com/memes/e0f221253de3a3d2282072561453b45f.jpg'
     await message.bot.send_photo(chat_id=message.chat.id,
                                     photo=types.InputFile.from_url(url))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)