from Predetors import Predator


class Lion(Predator):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)

    def printSize(self):
        print("Big")
    def makeNoise(self):
        print("BAAAAAAA")

    def __str__(self):
        return super().__str__()



