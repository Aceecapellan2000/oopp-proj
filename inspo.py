from flask import Flask, render_template
import shelve
app = Flask(__name__)

d = shelve.open('database.db.sql')
d['inspweighturl'] = ['https://www.youtube.com/embed/bMM3Kxb0-SU?autoplay=1', 'https://www.youtube.com/embed/bMM3Kxb0-SU?autoplay=1', 'https://www.youtube.com/embed/2N1GpPNXXXw?autoplay=1', 'https://www.youtube.com/embed/YErcj40hsXA?autoplay=1']
d['inspdieturl'] = ["https://www.youtube.com/embed/jqOK2hsCKRM?autoplay=1", "https://www.youtube.com/embed/mDHGaU_jGrQ?autoplay=1", "https://www.youtube.com/embed/8_3_8eaMsNM?autoplay=1", "https://www.youtube.com/embed/ZBR6METqbcQ?autoplay=1"]
d['inspsleepurl'] = ["https://www.youtube.com/embed/Ok93skBEXa0?autoplay=1", "https://www.youtube.com/embed/m_ZHgD5rVPU?autoplay=1", "https://www.youtube.com/embed/j5Sl8LyI7k8?autoplay=1", "https://www.youtube.com/embed/s3vaI15ICQg?autoplay=1"]
d['category'] = ['WEIGHT', 'DIET', 'SLEEP']
d.close()

@app.route("/login")
def login():
    return render_template("login.html", login=login)

@app.route("/survey")
def survey():
    return render_template("survey.html", survey=survey)

@app.route("/signup")
def signup():
    return render_template("signup.html", signup=signup)

@app.route("/inspiration")
def insp_weight():
    d = shelve.open('database.db.sql')
    user_attribute = 'sleep'
    if user_attribute == 'weight':
        url1 = d['inspweighturl'][0]
        url2 = d['inspweighturl'][1]
        url3 = d['inspweighturl'][2]
        url4 = d['inspweighturl'][3]
        category = d['category'][0]
    elif  user_attribute == 'diet':
        url1 = d['inspdieturl'][0]
        url2 = d['inspdieturl'][1]
        url3 = d['inspdieturl'][2]
        url4 = d['inspdieturl'][3]
        category = d['category'][1]
    else:
        url1 = d['inspsleepurl'][0]
        url2 = d['inspsleepurl'][1]
        url3 = d['inspsleepurl'][2]
        url4 = d['inspsleepurl'][3]
        category = d['category'][2]
    return render_template("insp_weight.html", url1=url1,url2=url2,url3=url3,url4=url4, category=category)

if __name__ == "__main__":
    app.run(debug = True)