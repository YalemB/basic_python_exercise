from Farms import Farm
class Hipo(Farm):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)

    def makeNoise(self):
        print("POPOP")

    def printSize(self):
        print("HUGA")

    def __str__(self):
        return super().__str__()
