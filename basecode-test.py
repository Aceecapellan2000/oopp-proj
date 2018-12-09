##test code, not actual/to be based off of
# age and gender affects possible amt of exercise and diet, i.e bigger amt for ages 18-30 then gradually decrease
# height & weight used to calculate bmi, bmi ranges for age and demographic to be keyed in
# bmi major factor that determines healthiness
# fitness accounts for natural health state, takes terminal conditions into account and balances health from there
# lifestyle accounts for how much time/expenses you can make for exercise
# em = early morning, n = night,
class UserInfo:
    __age = ''
    __gender = ''
    __height = ''
    __weight = ''
    __diet = ''
    __bmi = ''

    def __init__(self, age, gender, height, weight, diet):
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

    def getBMI(self):
        return self.__bmi

    def setBMI(self, bmi):
        self.__bmi = self.__weight/self.get_height()*self.get_height()


class Extra(UserInfo):
    def __init__(self, age, gender, height, weight, diet, fitness, lifestyle):
        super().__init__(age, gender, height, weight, diet)
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