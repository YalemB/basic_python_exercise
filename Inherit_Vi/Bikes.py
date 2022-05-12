from Vehicles import Vehicles

class Bike(Vehicles):
    def __init__(self, color, model, wheels, helmet):
        super().__init__(color, model, wheels)
        self.__helmet = helmet

    def getHelmet(self):
        print(self.__helmet)

    def setHelmet(self, helmet):
        self.__helmet = helmet

    def __str__(self):
        return "*******Bike******\n" + super().__str__() + "\n" + "Do have helmet: " + self.__helmet + "\n"
