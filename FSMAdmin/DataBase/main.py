import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import *
import sqlite3 as sq
button_load = KeyboardButton('/register')
button_delete = KeyboardButton('/cancel')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
    .add(button_delete)
def sql_start():
    global base
    global  cur
    base = sq.connect("pizza_cool.db")
    cur = base.cursor()
    if base:
        print('data base connect OK!')
    base.execute('create table if not exists menu(img TEXT, name TEXT , descroption TEXT, price TEXT);')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        # base = sq.connect("pizza_cool.db")
        # cur = base.cursor()
        cur.execute('insert into menu values(?, ?, ?, ?)', tuple(data.values))
        base.commit()

# token = '5351490636:AAEI4-V03agUU80kmg5ymmkvGu15hnxEYcU'

token = '5376697948:AAFEiaoQgPM0b7seTwqGuMAyCVFj6_Fh2rs'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

ID = None
class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

@dp.message_handler(commands=['start'])
async def cm_welcome(message: types.Message):
    global ID
    ID = message.from_user.id
    await message.answer("HI", reply_markup=button_case_admin)

@dp.message_handler(commands=['register'])
async def cm_start(message: types.Message):
    # if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply("Загрузи фото")


@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи названте")


@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Введи опесание")


@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("теперь  укажи цену")


@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await sql_add_command(state)
        await state.finish()


@dp.message_handler(state="*", commands=['cancel'])
@dp.message_handler(Text(equals='cancel', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    # if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Ok')





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    sql_start()
