import sqlite3
conn = sqlite3.connect('botbase.db')
getData = conn.execute('select * from data;')
for data in getData:
    print(data)

conn.commit()
conn.close()
