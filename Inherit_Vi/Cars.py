from Vehicles import Vehicles

class Car(Vehicles):
    def __init__(self, color, model, wheels, year):
        super().__init__(color, model, wheels)
        self.__year = year

    def getYear(self):
        print(self.__year)

    def setYear(self, year):
        self.__year = year

    def __str__(self):
        return "*******Car******\n" + super().__str__() + "\n" + str(self.__year) + "\n"
