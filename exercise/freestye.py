# get 2 numbers from user and print max number
# get 3 numbers from user and print max number
#
# n1 = int(input("Enter num: "))
# n2 = int(input("Enter num: "))
# n3 = int(input("Enter num: "))


# # if n1 > n2:
# #     print("max number is: ", n1)
# # else:
# #     print("max number is: ", n2)
#
# if n1 > n2 and n1 > n3:
#     print("max number is: ", n1)
# elif n2 > n3:
#     print("max number is: ", n2)
# elif n3 != n2:
#     print("max number is: ", n3)
# else:
#     print("all the numbers equal")
#
# hours = int(input("How many hours: "))
# year = int(input("car year: "))
# electric = input("car electric ? Y/N : ")
#
# pay = 0
#
# if hours <= 3:
#     pay = hours * 20
# elif 3 < hours <= 5:
#     pay = hours * 15
# elif 5 < hours <= 24:
#     pay = hours * 10
# else:
#     pay = hours * 5
# print(pay)
# if year == 2022 and electric == "Y":
#     dis = pay * 0.20
#     print("Total payment : ", pay - dis)
# elif year == 2022:
#     dis = pay * 0.15
#     print("Total payment : ", pay - dis)
# else:
#     dis = pay * 0.10
#     print("Total payment : ", pay - dis)

# if car year == 2022 and "elctric" discount(20%)
# if car year ==2022 and not "elctric" discount(15%)
# all cars discount(10%)


# def dis(tic, lug, c):
#     res = 0
#     if lug <= 20:
#         d = tic * 0.20
#         res = tic - d
#         print("discount luggage of 20% =", res)
#     elif 20 < lug < 40:
#         d = tic * 0.25
#         res = tic - d
#         print("discount luggage of 25% =", res)
#     else:
#         d = tic * 0.30
#         res = tic - d
#         print("discount luggage of 30% =", res)
#     if c in ("1", "b"):
#         d = res * 0.05
#         res -= d
#         print("discount on class of 5% =",res)
#     else:
#         d = res * 0.01
#         res -= d
#         print("discount on class of 1% =",res)
#     return res
#
#
# ticket = int(input("Enter ticket price"))
# luggage = int(input("Enter luggage kg : "))
# c = input("What your class: ")
# print("Before any discount",ticket)
#
# dis(ticket, luggage, c)

# flyet price = loagth
# if l >=20 dis = 20 %
# if l 20-40 dis = 25 %
# if 40-100 dis = 30%
# dis on class
# if c =1 or b dis = 5%
# if tor dis = 1.5%
# giscount claculation


# l = [1, 8, 12, 48, -3, 14, 22, 15]
#
# i = 0
# while len(l) > i:
#     new_l= l
#     mid = len(new_l)//2
#     if l[mid] < i:
#         l[mid-1] = -l[mid-1]
#         l[mid+1] = -l[mid+1]
#         break
#     else:
#         l.remove(new_l[mid])
#
#
# print(l)

#
# def is_prime(num: float):
#     i = 2
#     while i < num:
#         if num % i == 0:
#             return False
#         i += 1
#     return True
#
#
# for i in range(100):
#     if is_prime(i):
#         print(i, end=" ")

# def squar(a, b):
#     if a * a == b:
#         return True
#     else:
#         return False


# def squar2(a, b):
#     x = a/b/b
#     y = int(a/b/b)
#     if x == y:
#         return True
#     else:
#         return False
#
#
# print(squar2(49, 7))
#
# class Room:
#     def __init__(self, windows, doors, length, heigth,wide):
#         self.windows = windows
#         self.doors = doors
#         self.length = length
#         self.heigth = heigth
#         self.wide = wide
#
#     def size(self):
#         print(self.length * self.heigth)
#
#     def __str__(self):
#         return f"windows: {self.windows}, Doors: {self.doors}, Length: {self.length},Heigth: {self.heigth}"
#
#
# a = Room(4, 1, 80, 4,8)

# print(a)

#
# class Home(Room):
#     def __init__(self):
#         self.room = list()
#
#     def add_Room(self,w,d,x,y,z):
#         self.room.append(Room(w,d,x,y,z))
#
#     def __str__(self):
#         return f"Home how has {self.room} rooms"
#
# my_home = Home()
# my_home.add_Room(3,1,5,5,5)
# print(my_home)

# def is_in_str(st):
#     for i in range(len(st)-1, -1, -1):
#         if st[i] == "!":
#             return True
#     return False
#
#
# x = "!fdfgdfhgfhfg1gfgdfdsfd"
# print(is_in_str(x))


def string_match(a, b):
  c = 0
  for i in range(len(a)-1):

    check = b[i:i + 2]
    sub = a[i:i + 2]
    if check == sub:
      c += 1
  return c

q = 'abc'
w = 'abc'
string_match(q,w)