import logging
from aiogram import Bot, Dispatcher, executor, types
from config import token
from menu_button import btn_start, btn_register

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

# __________________________Klient_CHAT_______________________________
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Assalomu aleykum NITSga\nxush kelibsiz!\nBu bot orqali siz IT kurslariga online royhatdan otishingiz mumkin!',
                         reply_markup=btn_start)


@dp.message_handler()
async def send_welcome(message: types.Message):
    # await message.delete()
    # if message.text == 'Royhatdan o`tish':
    #     await message.answer('Ismingizni kiriting:')
    # elif message.text == 'PhoneNumber':
    #     await bot.send_contact(chat_id=message.from_user.id, reply_to_message_id=)
    # elif message.text == 'Kurslar':
    #     await message.answer('Kurslar!', reply_markup=btn_register)
    # elif message.text=='<--Back':
    #     await message.answer('back', reply_markup=btn_start)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)