import sqlite3

with sqlite3.connect("company.db") as con:
    cur = con.cursor()

with sqlite3.connect("book.db") as con:
    book = con.cursor()
