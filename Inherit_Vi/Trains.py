from Vehicles import Vehicles

class Train(Vehicles):
    def __init__(self, color, model, wheels, speed):
        super().__init__(color, model, wheels)
        self.__speed = speed
        if self.__speed > 350:
            self.t = "fast ass train"
        else:
            self.t = "regular train"

    def getSpeed(self):
        print(self.__speed)

    def setSpeed(self, speed):
        self.__speed = speed
        if self.__speed > 350:
            self.t = "fast ass train"
        else:
            self.t = "regular train"
        return self.__speed

    def __str__(self):
        return "*******Train******\n" + super().__str__() + "\n" + "speed  of the train :" + str(
            self.__speed) + "\n" + self.t + "\n"