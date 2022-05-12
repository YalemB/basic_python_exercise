from Predetors import Predator


class Tiger(Predator):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)
    def printSize(self):
        print("Huge")
    def makeNoise(self):
        print("WAAAAAAA")

    def __str__(self):
        return super().__str__()
