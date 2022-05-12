from Farms import Farm


class Horse(Farm):
    def __init__(self, gender, isFertile):
        super().__init__(gender, isFertile)

    def makeNoise(self):
        print(" HIIIIIIIII.")

    def printSize(self):
        print("Big")

    def __str__(self):
        return super().__str__()
