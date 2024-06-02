import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, g

from FDataBase import FDataBase

DATABASE = '/tmp/flsk_hw.db'
DEBUG = True
SECRET_KEY = os.urandom(20).hex()

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'flsk_hw.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db_hw.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)