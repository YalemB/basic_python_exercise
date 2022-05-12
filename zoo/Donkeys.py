from Farms import Farm


class Donkey(Farm):
    def __init__(self, gender, isFertile):
        super().__init__(gender, isFertile)

    def makeNoise(self):
        print(" AAAA-E")

    def printSize(self):
        print("Medium")

    def __str__(self):
        return super().__str__()
