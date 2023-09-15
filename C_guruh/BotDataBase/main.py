import logging
import sqlite3
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from config import token
logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('botbase.db')
conn.execute('create table if not exists data(message text);')
conn.commit()

bot = Bot(token=token)
dp = Dispatcher(bot)

# __________________________KLIENT_CHAT_______________________________
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum tozolovchi botga hush kelibsiz!")
    # text = str(message.from_user.full_name),
    # conn = sqlite3.connect('botbase.db')
    # conn.execute('insert into data values(?)',text)
    # conn.commit()


# __________________________GROUP_CHAT_________________________________
@dp.message_handler(content_types=['photo', 'video', 'audio', '*gif'])
async def echo(message: types.Message):
    await message.delete()

@dp.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS,
                                        types.ContentType.LEFT_CHAT_MEMBER])
async def check_channel(message: types.Message):
    print(message)


@dp.message_handler()
async def echo(message: types.Message):
    data = datetime.now()
    d=f'{data.hour}:{data.minute}:{data.second}'
    if 'https' in message.text:
        await message.delete()
        await message.answer(f'{message.from_user.full_name} Reklama tarqatmang!')
    else:
        print(f"{d} {message.from_user.full_name}: {message.text}")
        text = str(f"{d} {message.from_user.full_name}: {message.text}"),
        conn = sqlite3.connect('botbase.db')
        conn.execute('insert into data values(?)', text)
        conn.commit()


if __name__ == '__main__':
    conn.close()
    executor.start_polling(dp, skip_updates=True)