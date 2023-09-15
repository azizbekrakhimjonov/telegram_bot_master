import logging
from aiogram import Bot, Dispatcher, executor, types

from C_guruh.other_bot.config import token

logging.basicConfig(level=logging.INFO)


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



# URL = 'https://youtube.com/shorts/XP2gwdnWdvM?feature=share'
# @dp.message_handler()
# async def cmd_image(message: types.Message):
    # await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))
    # photo = InputFile("FOREST.png")
    # await bot.send_photo(chat_id=message.chat.id, photo=photo)

# @dp.message_handler(commands=["video"])
# async def send_video(message: types.Message):
#     video = open("py.mp4", "rb")
#     await bot.send_video(message.chat.id, video=video)

@dp.message_handler()
async def send_video(message: types.Message):
    await  bot.send_document(chat_id=message.chat.id, document=('SQL_methods.txt','r'))





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)