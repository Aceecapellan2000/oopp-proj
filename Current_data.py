class Current_information:

    def __init__(self,weight,height,date,sleeping,BMI):
        self.__weight=weight
        self.__height=height
        self.__date=date
        self.__sleeping=sleeping
        self.__BMI=BMI

    def get_weight(self):
        return self.__weight

    def set_weight(self,weight):
        self.__weight=weight

    def get_height(self):
        return self.__height

    def set_height(self,height):
        self.__height=height

    def get_date(self):
        return self.__date

    def set_date(self,date):
        self.__date=date

    def get_sleeping(self):
        return self.__sleeping

    def set_sleeping(self,sleeping):
        self.__sleeping=sleeping

    def get_BMI(self):
        return self.__BMI

    def set_BMI(self,BMI):
        self.__BMI= self.get_weight/self.get_height()*self.get_height()
