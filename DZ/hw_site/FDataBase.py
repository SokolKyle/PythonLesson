import sqlite3
import time
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения с БД")
        return []

    def add_les(self, name, price, curs):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO curs VALUES(NULL, ?, ?, ?, ?)", (name, price, curs, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления курса в БД" + str(e))
            return False
        return True

    def get_curs(self, curs_id):
        try:
            self.__cur.execute(f"SELECT title, text, curs FROM curs WHERE id = {curs_id}")
            res = self.__cur.fetchone()
            if res:
                return res['title'], res['text'], res['curs']
        except sqlite3.Error as e:
            print("Ошибка получения курса в БД: " + str(e))

        return None, None, None

    def get_curse_annonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text, curs FROM curs ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса в БД: " + str(e))
        return []
