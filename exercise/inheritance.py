# class Person:
#     def __init__(self, name, ID):
#         self.__name = name
#         self.__ID = ID
#
#     def get_Name(self):
#         return self.__name
#
#     def get_ID(self):
#         return self.__ID
#
#     def setName(self, name):
#         self.__name = name
#         return self.__name
#
#     def setID(self, ID):
#         self.__ID = ID
#         return self.__ID
#
#     def __str__(self):
#         return self.__name + " " + str(self.__ID)
#
#     def makeVoice(self):
#         return "Huuuuuh"
#
#
# class Student(Person):
#     def __init__(self, name, ID, grade):
#         super().__init__(name, ID)
#         self.__grade = grade
#
#     def getGrade(self):
#         return self.__grade
#
#     def setGrade(self, grade):
#         self.__grade = grade
#
#     def __str__(self):
#         return super().__str__() + " " + str(self.__grade)

# st1 = Student("eli", 323232323, 80)
# print(st1)

class Vehicles:
    def __init__(self, color, model, wheels):
        self.__color = color
        self.__model = model
        self.__wheels = wheels

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color
        return self.__color

    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = model
        return self.__model

    def getWheels(self):
        return self.__wheels

    def setWheels(self, wheels):
        self.__wheels = wheels
        return self.__wheels

    def __str__(self):
        self.__inf = "color: " + self.__color + "\nmodel: " + str(self.__model) + "\nnum of wheels: " + str(
            self.__wheels)
        return self.__inf


class Car(Vehicles):
    def __init__(self, color, model, wheels, engine):
        super().__init__(color, model, wheels)
        self.__engine = engine

    def getEngine(self):
        return self.__engine

    def setEngine(self, engine):
        self.__engine = engine

    def __str__(self):
        return "*******Car******\n"+ super().__str__() + "\n" + self.__engine


class Bike(Vehicles):
    def __init__(self, color, model, wheels, halmet):
        super().__init__(color, model, wheels)
        self.__halmet = halmet

    def getHalmet(self):
        return self.__halmet

    def setHalmet(self, halmet):
        self.__halmet = halmet

    def __str__(self):
        return "*******Bike******\n"+ super().__str__() + "\n" +"Do have halmet: "+ self.__halmet


class Plane(Vehicles):
    def __init__(self, color, model, wheels, sites):
        super().__init__(color, model, wheels)
        self.__sites = sites
    def getSites(self):
        return self.__sites
    def setSites(self, sites):
        self.__sites = sites

# x = Car("Grey","SUBARU",4,"GU-21")
# y = Bike("Red","suzaki", 2, "Yes")
# x.setWheels(8)
# print(x)
# print(y)
