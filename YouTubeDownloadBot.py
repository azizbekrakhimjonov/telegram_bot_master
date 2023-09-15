import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
token = '5376697948:AAFEiaoQgPM0b7seTwqGuMAyCVFj6_Fh2rs'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

# __________________________Klient_CHAT_______________________________
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Assalomu aleykum NITSga\nxush kelibsiz!\nBu bot orqali siz IT kurslariga online royhatdan otishingiz mumkin!')


@dp.message_handler()
async def send_welcome(message: types.Message):
    url = "https://t-one-youtube-converter.p.rapidapi.com/api/v1/createProcess"

    querystring = {"url": f"{message.text}", "format": "mp3", "responseFormat": "json",
                   "regenerate": "true", "volume": "50", "stop": "17", "start": "1", "lang": "en"}

    headers = {
        "X-RapidAPI-Key": "0b765b51b6msh59006515055e2b2p1e1facjsnfa954e780c20",
        "X-RapidAPI-Host": "t-one-youtube-converter.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    music = response.json().get('YoutubeAPI').get('urlMp3')
    await message.answer(music)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)