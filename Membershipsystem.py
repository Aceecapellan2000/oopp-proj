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


if __name__ == "__main__":
    app.run(debug=True)
