import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = "6384532641:AAF0e8iMw_ZNb1HGqkr8Kz3-X5KsRPyCgTQ"
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



# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "chro xozayn nado???")
    await message.delete()


# @dp.message_handler(commands=['start'])
async def cm_start(message: types.Message):
    global ID
    ID = message.from_user.id
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply("Загрузи фото")

# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи названте")


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Введи опесание")


# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("теперь  укажи цену")


# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = (message.text)
        async with state.proxy() as data:
            await message.reply(str(data))
        await state.finish()


# @dp.message_handler(state="*", commands=['back'])
# @dp.message_handler(Text(equals='back', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    global ID
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Ok')

# @dp.message_handler(lambda message:'hello' in message.text)
# async def cancel_handler(message: types.Message):
#         await message.delete()
#         await message.answer('Salom')
#
# @dp.message_handler(lambda message:message.text.startswith("taksi"))
# async def cancel_handler(message: types.Message):
#         await message.delete()
#         await message.answer('TAkkkksi')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['/register'], state=None)
    dp.register_message_handler(load_photo,content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler,state="*", commands=['back'])
    dp.register_message_handler(cancel_handler,Text(equals='back', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)



if __name__ == '__main__':
    register_handler_admin(dp)
    executor.start_polling(dp, skip_updates=True)





