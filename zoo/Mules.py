from Farms import Farm

class Mule(Farm):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)
    def makeNoise(self):
        print("HI AAAAA")

    def printSize(self):
        print("Medium")

    def __str__(self):
        return super().__str__()
