from flask import Flask, render_template
import basecode_test

app = Flask('testapp')

@app.route('/')
def default():
    num = basecode_test.test
    return render_template('datapage.html', variable = int(num))

@app.route('/planpage')
def planpage():
    return render_template('planpage.html')

@app.route('/inspopage')
def inspopage():
    return render_template('inspopage.html')

if __name__ == "__main__":
    app.run(debug = True)
