import sqlite3


class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        """
        sallary - ish haqi
        execute - bajarmoq
        commit - topshirmoq
        EXISTS - mavjud
        items - buyumlar
        Storage - saqlash
        dataStorage - ma'lumotlarni saqlash
        Helper - yordamchi
        command - buyruq
        chat - suhbat
        substitute  - almashtirmoq
        primary - asosiy
        select - tanlang
        another  - boshqa
        process - jarayon
        data analysis - malumotlarni tahlil qilish
        methods - usullari
        append - qoshish
        insert - kiritmoq
        """
        stmt = "CREATE TABLE IF NOT EXISTS items (description text)"
        self.conn.execute(stmt) # execute - bajarmoq
        self.conn.commit() # commit - topshirmoq

    def add_item(self, item_text):
        stmt = "INSERT INTO items (description) VALUES (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM items WHERE description = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        stmt = "SELECT description FROM items"
        return [x[0] for x in self.conn.execute(stmt)]