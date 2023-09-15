# import requests
# TOKEN = "5351490636:AAEI4-V03agUU80kmg5ymmkvGu15hnxEYcU"
# chat_id = "52614426"
# text = "hello i am telegram echo bot with python"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
# r = requests.get(url)
# print(r)


import logging


from aiogram import Bot, Dispatcher, types

# bot_id = '-1001661816517'
# get_dataStorage = {"message_id": 1381, "from": {"id": 1486580350, "is_bot": False, "first_name": "Azizbek", "last_name": "Rahimjonov", "username": "azizbekrahimjonov571", "language_code": "ru"}, "chat": {"id": -1001661816517, "title": "Python C Guruh", "username": "python_c_gurux", "type": "supergroup"}, "date": 1653195383, "new_chat_participant": {"id": 2003049919, "is_bot": False, "first_name": "▓▒Hacked▒▓", "username": "python_007", "language_code": "en"}, "new_chat_member": {"id": 2003049919, "is_bot": false, "first_name": "▓▒Hacked▒▓", "username": "python_007", "language_code": "en"}, "new_chat_members": [{"id": 2003049919, "is_bot": false, "first_name": "▓▒Hacked▒▓", "username": "python_007", "language_code": "en"}]}
# token = '5351490636:AAEI4-V03agUU80kmg5ymmkvGu15hnxEYcU'
token = '6384532641:AAF0e8iMw_ZNb1HGqkr8Kz3-X5KsRPyCgTQ'
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message.from_user.id)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
        await message.bot.send_message("Bot id: ", bot.id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)