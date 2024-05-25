from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = "dsa567dsa7d5sad567as5das67"

menu = [
    {'url': 'index', 'name': 'Главное'},
    {'url': 'about', 'name': 'О нас'},
    {'url': 'contact', 'name': 'Обратная связь'},  # Example profile
]


@app.route("/")
@app.route("/index")
def index():
    # print(url_for('index'))
    return render_template('index.html',
                           title="Главное", menu=menu)


@app.route("/about")
def about():
    # print(url_for('about'))
    return render_template("about.html",
                           title="О нас", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно', category='success')
        else:
            flash('Ошибка отправки', category='error')
        # print(request.form)
        #
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template("contact.html", **context,
        #                        title="Обратная связь", menu=menu)
    return render_template("contact.html",
                           title="Обратная связь", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page404.html", title="Страница не найдена", menu=menu)


@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST" and request.form['username'] == 'admin' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    elif 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
