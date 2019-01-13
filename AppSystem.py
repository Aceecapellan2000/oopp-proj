from flask import Flask, render_template, request, flash, redirect, url_for, session
import basecode
import DataForm
import shelve
import bak

# name, age, gender, height, weight
app = Flask('testapp')
app.secret_key = 'secretkey'

# stores base data upon registering
@app.route('/', methods=['GET', 'POST'])
def register():
    form = DataForm.RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        d = shelve.open('database.db.sql')
        d['name'] = form.name.data
        d['age'] = form.age.data
        d['gender'] = form.gender.data
        d['height'] = form.height.data
        d['weight'] = form.weight.data
        d['bmi'] = round(form.weight.data/(form.height.data/100)**2)
        d['diet'] = form.diet.data
        flash('Thanks for registering')
        return redirect(url_for('default'))
    return render_template('flaskform.html', form=form)

# generates messages based on data
@app.route('/datapage')
def default():
    d = shelve.open('database.db.sql')
    username = d['name']
    bmi = d['bmi']
    diet = d['diet']
    sleep = 0
    p1 = basecode.calcBMI(bmi)
    p2 = basecode.calcDiet(diet)
    p3 = basecode.calcSleep(8)
    num = basecode.calcOverall(p1, p2, p3)
    maj = basecode.get_majcomp(p1[1], p2[1], p3[1])
    m = basecode.Message(maj, bmi, sleep)
    base = basecode.getStr(bmi)
    if bmi > 25:
        plan = 'reduce carbohydrate and fat intake (tip: no fried food!)'
        run = 'run 2km twice a week'
        eta = 'estimated time to reach optimum BMI: 3 months'
        points = bmi - 25
    elif bmi >18:
        plan = 'maintain portions, but do throw in more fiber! (banana oatmeal for breakfast?)'
        run = 'run 1km once a week'
        eta = 'stay healthy!'
        points = ''
    else:
        plan = 'increase carbohydrate and fat intake (think: noodles & meat)'
        run = 'run 1km once a week'
        eta = 'estimated time to reach optimum BMI: 2 months'
        points = 18 - bmi
    return render_template('datapage.html', variable = int(num), nom = username, bmi = bmi, m=m, base = base.format(bmi, points), plan = plan, run = run, eta = eta)

@app.route('/planpage')
def planpage():
    return render_template('planpage.html')

@app.route('/inspopage')
def inspopage():
    return render_template('inspopage.html')

@app.route('/statspage')
def statspage():
    return render_template('statspage.html')

if __name__ == "__main__":
    app.run(debug = True, port='80')
