import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5375176127:AAG-BAeAEYR2EAS96zl7CtrV3CS9hmleNvk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    print(message.from_user.first_name)
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}', reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)
    if message.text == '♦ Random Number':
        # await bot.send_message(message.from_user.id, "" + str(random.randint(1000, 9999)))
        await bot.send_message(message.from_user.id, "" + str(random.randint(1000, 9999)))

    elif message.text == '🍕 Random String':
        await bot.send_message(message.from_user.id, '🍕 Random String', reply_markup=nav.subFoodMenu)

    elif message.text == '⬅ Main Menu':
        await bot.send_message(message.from_user.id, "⬅ Main Menu", reply_markup=nav.mainMenu)

    elif message.text == '➡ Other':
        await bot.send_message(message.from_user.id, "➡ Other", reply_markup=nav.otherMenu)

    elif message.text == '⬅ Back':
        await bot.send_message(message.from_user.id, '⬅ Back', reply_markup=nav.otherMenu)

    elif message.text == '📚 Information':
        await bot.send_message(message.from_user.id, "📚 Information", reply_markup=nav.subOtherMenu)

    elif message.text == '📈 Exchange Rate':
        await bot.send_message(message.from_user.id, "📈 Exchange Rate")

    else:
        await message.reply('No data')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
