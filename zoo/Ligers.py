from Predetors import Predator


class Liger(Predator):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)


    def makeNoise(self):
        print("BAAAAAAA")

    def printSize(self):
        print("Big")

    def __str__(self):
        return super().__str__()
