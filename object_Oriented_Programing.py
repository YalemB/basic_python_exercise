# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def __str__(self):
#         return f"{self.__name} is {self.__age} years old  "
#
#     def getName(self):
#         return self.__name
#     def setName(self):
#         return self.__name
#     def getAge(self):
#         return self.__age

#     def setAge(self, age):

#         if age < 22:
#             self.__age = age
#         else:
#             print("can't update")
#
# student1 = Student("eli", 27)
# print(student1)
# print(student1.getName())
# student1.setName("BOI")
# print(student1)
#
#
# class Car:
#     def __init__(self, wheels, model, year, price):
#         self.__wheels = wheels
#         self.__model = model
#         self.__year = year
#         self.__price = price
#         if self.__wheels < 4:
#             self.__wheels = 4
#
#     def getWheels(self):
#         return self.__wheels
#
#     def getModel(self):
#         return self.__model
#
#     def getYear(self):
#         return self.__year
#
#     def getPrice(self):
#         return self.__price
#
#     def setWheels(self, wheels):
#         self.__wheels = wheels
#         return self.__wheels
#
#     def setModel(self,model):
#         self.__model = model
#         return self.__model
#
#     def setYear(self,year):
#         self.__year = year
#         return self.__year
#
#     def setPrice(self,price):
#         self.__price = price
#         return self.__price
#
#
#     def __str__(self):
#         return f"model {self.__model} year {self.__year} price {self.__price}"
#
#
# subaru = Car(4, "impreza", 2014, 3400)
# hunda = Car(4,"civic",2017, 75000)
# skuda = Car(2,"f\abia",2018,80000)
# l=[subaru.getPrice(),hunda.getPrice(),skuda.getPrice()]
# print(max(l))


#
# class Square:
#     def __init__(self, area=30, color="red"):
#         self.__area = area
#         self.__color = color
#
#     def sq_draw(self):
#         self.k = self.__area // 4
#         self.m = "*" + " " * (((self.k)*3)-4) + "*"
#
#         for j in range(self.k):
#             print("*", end="  ")
#         print("")
#         for t in range(self.k-2):
#             print(self.m)
#         for y in range(self.k):
#             print("*", end="  ")
#         print("")
#         return f"square area= {self.__area} "
#
#     # def sq_draw(self):
#     #     self.k = self.__area // 4
#     #     self.s = "*"
#     #     return f"{self.s*self.k}\n",
#
#
# print(Square().sq_draw())

#
#
#
#
# class triangl:
#     def __init__(self, area=20, color="red"):
#         self.__area = area
#         self.__color = color


# area = 20
#
# k = area // 4
# s = "* " * k
# for i in range(k):
#     print(s)

#
# class Apartment:
#     def __init__(self, address, home_num, buy_price, avg_rent):
#         self.__address = address
#         self.__home_num = home_num
#         self.__buy_price = buy_price
#         self.__avg_rent = avg_rent
#
#     def Yield_percent(self):
#         self.res = self.__buy_price * 100 // (self.__avg_rent * 12)
#         return f"Yield percent = {self.res} "
#
#
# my_home = Apartment("Brazil", 100, 1000000, 4000)
# print(my_home.Yield_percent())


# class Cat:
#     def __init__(self, name, hair_color, age):
#         self.__name = name
#         self.__age = age
#         self.__hair_color = hair_color
#
#     def what_sound(self):
#         return "me-yho"
#
#     def is_mostash(self, mustache):
#         if mustache == "yes":
#             return f"yes {self.__name} do's have mustache"
#         else:
#             return f"No {self.__name} don't have mustache"
#     def __str__(self):
#         return f"******* Cat info *******\nname: {self.__name} \ncolor: {self.__hair_color} \nage: {self.__age}"
#
#
# class Dog:
#     def __init__(self, name, breed, color):
#         self.__name = name
#         self.__breed = breed
#         self.__color = color
#
#     def what_sound(self):
#         return "How-how"
#     def is_bites(self,bites):
#         if bites == "yes":
#             return f"yes {self.__name} do bites be careful!"
#         else:
#             return f"No {self.__name} do not bites."
#     def __str__(self):
#         return f"******* Dog info *******\nname: {self.__name} \nbreed: {self.__breed} \ncolor: {self.__color}"
#


# ca1 = Cat("ketti","grey",12)
# dog1 = Dog("nala","dogo","white")
# # print(ca1.what_sound(),"\n",ca1.is_mostash("yes"))
# # print(dog1.what_sound(),"\n",dog1.is_bites("no"))
# print(dog1)
# print(ca1)
# import datetime
#
#
# class Students:
#     def __init__(self, name, ID, meth_g, history_g, literature_g, gred, birth_date):
#         self.__name = name
#         self.__id = ID
#         self.__meth_g = meth_g
#         self.__history_g = history_g
#         self.__literature_g = literature_g
#         self.__gred = gred
#         self.__birth_date = birth_date
#
#     def get_meth_g(self):
#         return self.__meth_g
#
#     def get_history_g(self):
#         return self.__history
#
#     def get_literature_g(self):
#         return self.__literature_g
#
#     def set_meth_g(self, meth_g):
#         self.__meth_g = meth_g
#         return self.__meth_g
#
#     def set_history_g(self, history_g):
#         self.__history = history_g
#         return self.__history
#
#     def set_literature_g(self, literature_g):
#         self.__literature_g = literature_g
#         return self.__literature_g
#
#     def age(self):
#         currentDateTime = datetime.datetime.now()
#         date = currentDateTime.date()
#         self.__age = date.year - self.__birth_date
#         return self.__age
#
#     def avg(self):
#         self.__avg = round((self.__meth_g + self.__history_g + self.__literature_g) / 3, 2)
#         return self.__avg
#
#     def __str__(self, ):
#         self.txt = f"""*** Student info***\nname: {self.__name}\nAge:{self.age()} \nID: {self.__id}\nGred: {self.__gred}
#                     \t--Greads--\n\t\t\t[meth:{self.__meth_g},history:{self.__history_g},literature:{self.__literature_g}]
#                      Greads average:\n\t\t\t\t\t\t{self.avg()}"""
#         if self.avg() > 90:
#             return self.txt + "\n\t\t\t\tGraduated with honors!\n"
#         elif self.avg() < 60:
#             return self.txt + "\n\t\t\t\t\t   Failed!\n"
#         else:
#             return self.txt + "\n\t\t\t\t\t   Passed!"
#
#
# s1 = Students("Adi", 123408821, 72, 67, 82, 10, 1994)
# s2 = Students("Forlan", 523408825, 96, 9, 77, 12, 1990)
# s3 = Students("Goarg", 323408823, 90, 9, 100, 9, 1998)
# s4 = Students("Zlatan", 11111111, 10, 10, 100, 100, 1982)
#
# # def top_students():
# #     if s1.avg() > s2.avg() and s1.avg() > s3.avg() and s1.avg() > s4:
# #         print("$$$$$ TOP STUDENT $$$$$\n", s1)
# #     elif s2.avg() > s1.avg() and s2.avg() > s3.avg() and s2.avg() > s4.avg():
# #         print("$$$$$ TOP STUDENT $$$$$\n", s2)
# #     elif s3.avg() > s1.avg() and s3.avg() > s2.avg() and s3.avg() > s4.avg():
# #         print("$$$$$ TOP STUDENT $$$$$\n", s3)
# #     else:
# #         print("$$$$$ TOP STUDENT $$$$$\n", s4)
# # top_students()
# l = [s1, s2, s3, s4]
#
#
# def top_stud():
#     maximum = l[0].avg()
#     G= l[0]
#
#     for i in range(len(l)):
#         if l[i].avg() > maximum:
#             maximum = l[i].avg()
#             G = l[i]
#     print("\t\t\t\t\t$$$$$ TOP STUDENT $$$$$\n")
#     print(G)
#
# top_stud()
