class Vehicles:
    def __init__(self, color, model, wheels):
        self.__color = color
        self.__model = model
        self.__wheels = wheels

    def getColor(self):
        print(self.__color)

    def setColor(self, color):
        self.__color = color
        return self.__color

    def getModel(self):
        print(self.__model)

    def setModel(self, model):
        self.__model = model
        return self.__model

    def getWheels(self):
        print(self.__wheels)

    def setWheels(self, wheels):
        self.__wheels = wheels
        return self.__wheels

    def __str__(self):
        self.__inf = "color: " + self.__color + "\nmodel: " + str(self.__model) + "\nnum of wheels: " + str(
            self.__wheels)
        return self.__inf
