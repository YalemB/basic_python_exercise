from Mammals import Mammal

class Predator(Mammal):
    def __init__(self, isMale, isFertile):
        super().__init__(isMale, isFertile)

    def prey(self):
        print("YAMI")


    def __str__(self):
        return super().__str__()
