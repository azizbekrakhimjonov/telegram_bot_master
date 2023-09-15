import logging

from aiogram import Bot, Dispatcher, executor, types


from config import token

logging.basicConfig(level=logging.INFO)


bot = Bot(token=token)
dp = Dispatcher(bot)

# __________________________KLIENT_CHAT_______________________________
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum tozolovchi botga hush kelibsiz!")


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
    if 'salom' in message.text:
        await message.delete()
        await message.answer(f'{message.from_user.full_name} Reklama tarqatmang!')
    else:
        print(f"{message.from_user.full_name}: {message.text}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)