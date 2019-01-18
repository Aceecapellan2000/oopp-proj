from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/mainpage')
def mainpage():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index2.html')


@app.route('/summary')
def summary():
    return render_template('index3.html')


@app.route('/voucher')
def voucher():
    return render_template('index4.html')


@app.route('/aches')
def aches():
    return render_template('index6.html')


@app.route('/article')
def article():
    return render_template('index5.html')


@app.route('/diabetes')
def diabetes():
    return render_template('index7.html')


@app.route('/stigma')
def stigma():
    return render_template('index8.html')



if __name__ == "__main__":
    app.run(debug=True)
