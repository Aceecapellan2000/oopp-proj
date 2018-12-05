##test code, not actual
class User:
    __name = ''
    __age = ''
    __height = ''
    __weight = ''
    __diet = ''

    def __init__(self, name, age, height, weight, diet):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__diet = diet

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def getBMI(self):


