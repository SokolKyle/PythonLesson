import sqlite3

prog_lang = [
    ("C", 1972, "Деннис Ритчи"),
    ("Java", 1995, "Джеймс Гослинг"),
    ("Python", 1991, "Гвидо ван Россум"),
    ("JavaScript", 1995, "Брендан Эйх"),
    ("C++", 1985, "Бьёрн Страуструп"),
    ("C#", 2000, "Андерс Хейлсберг"),
    ("PHP", 1994, "Расмус Лердорф"),
    ("Ruby", 1995, "Юкихиро Мацумото"),
    ("Swift", 2014, "Крис Латтнер"),
    ("Kotlin", 2011, "Янг Чжеттер")
]

with sqlite3.connect("Program_lang.db") as con:
    cur = con.cursor()
    cur.execute("""
         CREATE TABLE IF NOT EXISTS lan(
             lan_id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             age INTEGER,
             author TEXT
         )
         """)
    for lang in prog_lang:
        cur.execute("INSERT INTO lan VALUES(NULL, ?, ?, ?)", lang)
