import json
import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor

from bot_send_photoVideo.config import token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)

connloc = sqlite3.connect("request.db") #open the database


@bot.command("start") #function active when typing on the telegram /start chat
def start_command(chat, message, args, keyboard_selection=None):
    bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'text': 'Welcome, what do you want to do?',
        'reply_markup': json.dumps(keyboard_selection)}) #sending a message in Json style
    item = chat.id
    item2 = "db"+str(chat.id)
    try:
        sqlloc = ("create table {} (" \
        " chat_id INTEGER NOT NULL PRIMARY KEY,"\
        " locpar varchar(20)," \
        " stoppar varchar(20)," \
        " locdes varchar(20) ," \
        " stopdes varchar(20));".format(item2))
        connloc.execute(sqlloc)
        cloc = connloc.cursor()
        cloc.execute("INSERT INTO {}(chat_id) VALUES (?);".format(item2), (item,))
        connloc.commit()
    except:
        return #after command /start, create a new table in the database, if it already exists, because this bot is an always active bot (there are other choices besides the /start)




        return

@bot.message_matches('Look for your stop times now')
def send_lol(chat, message, keyboard_locpo=None):
     bot.api.call('sendMessage', {
        'chat_id': chat.id,
        'text': 'Well select your town',
        'reply_markup': json.dumps(keyboard_locpo)}) #This function allows you to choose the city where you are, in fact the reply markup is the telegram keyboard containing all the cities





#This is the first function (@bot.process) that analyzes the first message sent by the initial function (which allows you to choose the city). It inserts your choice in the database if what you have written is equal to at least one of the cities containing in the result list
@bot.process_message()#  He then enters the city in the locpar box (where the departure cities are located). And finally a keyboard is activated that allows you to choose one of the stops in your city
def name_loc(chat, message):
    item = chat.id
    item3 = "db"+str(chat.id)
    cloc = connloc.cursor()
    varcheck = cloc.execute("SELECT * FROM {} WHERE chat_id= (?)".format(item3), (item,))
    varop = []
    for items in varcheck:
        for items2 in items:
            varop.append(items2)
    for i in result:
        if message.text == i and varop[1] == None and varop[2] == None and varop[3] == None and varop[4] == None:
            item = i
            item2 = chat.id
            cloc = connloc.cursor()
            cloc.execute("UPDATE {} SET locpar = (?) WHERE chat_id = (?);".format(item3), (item,item2))
            connloc.commit()
            for t in result[i]:
                        keyboard_stops = {"keyboard": [[{"text": t} for t in pair] for pair in zip(result[i])]}
            bot.api.call('sendMessage', {
                            'chat_id': chat.id,
                            'text': 'Perfect, choose your stop bus',
                            'reply_markup': json.dumps(keyboard_stops)}) #fermata 1






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)