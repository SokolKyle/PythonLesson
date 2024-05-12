import sqlite3

# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
#     # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 35000)")
#     # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 45000)")
#     # cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 75000)")
#     # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 45000)")
#
# con.commit() #- сохраняет все изменения в БД
# con.close() #- закрывает соединение с БД

# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000),
#     INSERT INTO cars VALUES(NULL, 'Volvo', 35000),
#     INSERT INTO cars VALUES(NULL, 'Mercedes', 45000)
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()
