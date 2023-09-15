import sqlite3
conn = sqlite3.connect('dataStorage.db')
cur = conn.cursor()
cur.execute("""create table if not exists message(data text);""")

data_user = 'Abdurahmon',
cur.execute(f"insert into message values(?)", data_user)
conn.commit()
conn.close()