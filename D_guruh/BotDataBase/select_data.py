import sqlite3
conn = sqlite3.connect('dataStorage.db')
cur = conn.cursor()
get_data = cur.execute('select *from message;')
# print(get_data.fetchall())
for i in get_data:
    print(i)