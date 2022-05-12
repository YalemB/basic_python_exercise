from Mammals import Mammal


class Farm(Mammal):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)


    def gallop(self):
        print("CLOCK-CLICK")

    def __str__(self):
        return super().__str__()
