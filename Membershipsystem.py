from flask import Flask, render_template, redirect, url_for, request, session
from persistence import *


application = Flask(__name__)
application.config.from_mapping(
    SECRET_KEY = 'xyz'
)


@application.route('/', methods=['GET', 'POST'])
@application.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid credentials, please try again'
        else:
            session['username'] = username
            add_login_points(username)
            return redirect(url_for('mainpage'))
    return render_template('login.html', error=error)


@application.route('/mainpage')
def mainpage():
    point = get_member(session['username'])
    return render_template('home.html', point=point)


@application.route('/home')
def home():
    point = get_member(session['username'])
    return render_template('history.html', point=point)


@application.route('/voucher')
def voucher():
    voucher_redemption(session['username'])
    return render_template('voucher.html')


@application.route('/aches')
def aches():
    return render_template('aches.html')


@application.route('/article')
def article():
    add_member_points(session['username'])
    return render_template('articles.html')


@application.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')


@application.route('/stigma')
def stigma():
    return render_template('stigma.html')


@application.route('/apps')
def apps():
    add_member_points(session['username'])
    return render_template('apps.html')


@application.route('/reset')
def reset():
    members.clear()
    member = Points('admin', 100, 1, 200, 300)

    add_member(member)
    return 'Add admin member'


if __name__ == "__main__":
    application.run(debug=True)
