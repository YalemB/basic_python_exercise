from Vehicles import Vehicles

class Plane(Vehicles):
    def __init__(self, color, model, wheels, sites):
        super().__init__(color, model, wheels)
        self.__sites = sites

    def getSites(self):
        print(self.__sites)

    def setSites(self, sites):
        self.__sites = sites
        return self.__sites

    def sitPlace(self):
        self.s_n = int(input("what your site number: "))
        if self.s_n % 3 == 0:
            self.s_p = "you site is by the window."
        else:
            self.s_p = "Not window site"
        print(self.s_p)

    def __str__(self):
        return "*******Plane******\n" + super().__str__() + "\n" + "number of sites: " + str(self.__sites)+"\n"
