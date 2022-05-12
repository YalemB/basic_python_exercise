class Mammal():
    def __init__(self, isMale, isFertile):
        self.__isMale = isMale
        self.__isFertile = isFertile

    def getisMale(self):
        return self.__isMale

    def setisMale(self, isMale):
        self.__isMale = isMale
        return self.__isMale

    def getisFertile(self):
        return self.__isFertile

    def setisFertile(self, isFertile):
        self.__isFertile = isFertile
        return self.__isFertile

    def printData(self):
        if self.__isMale:
            self.M ="Male"
        else:
            self.M = "Female"
        if self.__isFertile:
            self.F = "isFertile"
        else:
            self.F = "is not Fertile"
        print(self.M + "\\" + self.F)


    def __str__(self):
        return f"Is Male: {self.__isMale}\nIs fertile: {self.__isFertile}\n"
