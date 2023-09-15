import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from config import token
logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

conn = sqlite3.connect('dataStorage.db')
cur = conn.cursor()
cur.execute("""create table if not exists message(
                        id text,
                        first_name text, 
                        last_name text
                        );""")
conn.commit()
conn.close()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message.from_user.first_name)
    await message.reply("Assalomu aleykum")
    conn = sqlite3.connect('dataStorage.db')
    cur = conn.cursor()
    data_user = message.from_user.id,message.from_user.first_name, message.from_user.last_name
    cur.execute(f"insert into message values(?,?,?)", data_user)
    conn.commit()
    conn.close()

@dp.message_handler(commands=['members'])
async def send_welcome(message: types.Message):
    conn = sqlite3.connect('dataStorage.db')
    cur = conn.cursor()
    get_data = cur.execute('select *from message;')
    await message.reply(f"Users: {get_data.fetchone()}")
    conn.close()
@dp.message_handler(commands=['all_users'])
async def send_welcome(message: types.Message):
    conn = sqlite3.connect('dataStorage.db')
    cur = conn.cursor()
    get_data = cur.execute('select count (*) from message;')
    await message.reply(f"Users: {get_data.fetchall()}")
    conn.close()

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
