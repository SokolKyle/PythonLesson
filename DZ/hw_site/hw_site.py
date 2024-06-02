import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, g
from FDataBase import FDataBase

DATABASE = '/tmp/hw.db'
DEBUG = True
SECRET_KEY = os.urandom(20).hex()

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'hw.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
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
    return render_template("index.html", menu=dbase.get_menu(), curse=dbase.get_curse_annonce())


@app.route("/add_les", methods=["GET", "POST"])
def add_les():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['price']) > 7 and len(request.form['curs']) > 10:
            res = dbase.add_les(request.form['name'], request.form['price'], request.form['curs'])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курс добавлен успешно", category='success')
        else:
            flash("Ошибка добавления курса", category='error')

    return render_template("add_les.html", menu=dbase.get_menu(), title="добавление курса")


@app.route("/curs/<int:id_curs>")
def show_curs(id_curs):
    db = get_db()
    dbase = FDataBase(db)
    title, text, curs = dbase.get_curs(id_curs)

    return render_template("curs.html", menu=dbase.get_menu(), title=title, text=text, curs=curs)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
