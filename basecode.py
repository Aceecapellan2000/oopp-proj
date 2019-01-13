## all base functions/conditionals stored here (refer to AppSystem.py)
# age and gender affects possible amt of exercise and diet, i.e bigger amt for ages 18-30 then gradually decrease
# height & weight used to calculate bmi, bmi ranges for age and demographic to be keyed in
# bmi major factor that determines healthiness
# fitness accounts for natural health state, takes terminal conditions into account and balances health from there
# lifestyle accounts for how much time/expenses you can make for exercise
# em = early morning, n = night, fd = full day, bm = bare minimum

import jinja2

class UserInfo:
    __name = ''
    __age = ''
    __gender = ''
    __height = ''
    __weight = ''
    __diet = ''
    __bmi = ''

    def __init__(self, name, age, gender, height, weight, diet):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__height = height
        self.__weight = weight
        self.__diet = diet

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_diet(self):
        return self.__diet

    def set_diet(self, diet):
        self.__diet = diet

    def getBMI(self):
        return self.__bmi

    def setBMI(self, bmi):
        self.__bmi = self.__weight / self.get_height() * self.get_height()

    def __str__(self):
        s = '{} {} {} {} {} {}'.format(self.__name, self.__age, self.__gender, self.__height, self.__weight, self.__diet)
        return s



class Extra(UserInfo):
    def __init__(self, name, age, gender, height, weight, diet, fitness, lifestyle):
        super().__init__(name, age, gender, height, weight, diet)
        self.__fitness = fitness
        self.__lifestyle = lifestyle

    def get_fitness(self):
        return self.__fitness

    def set_fitness(self, fitness):
        self.__fitness = fitness

    def get_lifestyle(self):
        return self.__lifestyle

    def set_lifestyle(self, lifestyle):
        if lifestyle == 'student':
            self.__lifestyle = 'em, n, weekend'
        elif lifestyle == 'part-time' or 'stay at home':
            self.__lifestyle = 'fd, em, n'
        else:
            self.__lifestyle = 'bm, em, n'

# calculates score bmi adds to health meter (max 50)
def calcBMI(bmi):
    health = 0
    ratio = 0
    if bmi < 18:
        health =+ 40
        ratio =+ 10
    elif bmi < 25:
        health =+ 50
        ratio =+ 0
    elif bmi < 30:
        health =+ 40
        ratio =+ 10
    elif bmi < 40:
        health =+ 30
        ratio =+ 20
    else:
        health =+ 20
        ratio =+ 30
    return health, ratio

# calculates sleep cont. to health meter (max 20)
def calcSleep(sleep):
    health = 0
    ratio = 0
    if sleep >= 11:
        health =+ 0
        ratio =+ 20
    elif sleep >= 9:
        health =+ 10
        ratio =+ 10
    elif sleep >= 6:
        health =+ 20
        ratio =+ 0
    elif sleep >= 4:
        health =+ 10
        ratio =+ 10
    else:
        health =+ 0
        ratio =+ 20
    return health, ratio

# calculates diet point contribution to health meter (max 30 [for now])
# input specifics!!!!!!!
def calcDiet(diet):
    health = 0
    ratio = 0
    if diet == 'balanced':
        health =+ 30
        ratio =+ 0
    elif diet == 'slight':
        health =+ 20
        ratio =+ 10
    else:
        health =+ 10
        ratio =+ 20
    return health, ratio

# identifies main cause of affected health, using max ratio
def get_majcomp(bmi, diet, sleep):
    list1 = [bmi, diet, sleep]
    if list1 == [0, 0, 0]:
        s = 'none'
    elif max(list1) == bmi:
        s = 'bmi'
    elif max(list1) == diet:
        s = 'diet'
    else:
        s = 'sleep'
    return s

# returns main message header based on problem identified
def Message(s, bmi, sleep):
    if s == 'none':
        msg = 'WAY TO GO!'
    elif s == 'bmi':
        msg = ''
        if bmi < 18:
            msg = 'IMPROVE YOUR DIET!'
        else:
            msg = 'EXERCISE MORE!'
    elif s == 'diet':
        msg = 'IMPROVE YOUR DIET!'
    else:
        if sleep >= 11:
            msg = 'TOO MUCH SLEEP'
        else:
            msg = 'GET MORE SLEEP!'
    return msg

# calculates message if bmi is main cause of low health
def getStr(bmi):
    s = ''
    if bmi < 18:
        s = 'Your BMI is {}, {} points below healthy range. You can improve this by being more active (build muscle) or improving your diet.'
    elif bmi < 25:
        s = 'Your bmi range is optimum. Keep it up! Any goals you want to pursue?'
    else:
        s = 'Your BMI is {}, {} points above healthy range. You can improve this by being more active or improving your diet.'
    return s

# calculates overall score on health meter
def calcOverall(bmi, diet, sleep):
        health = bmi[0] + diet[0] + sleep[0]
        return health

class StoreHealth():
    def __init__(self, health):
        self.health = health

    def __int__(self):
        return self.health

