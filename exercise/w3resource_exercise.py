# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)

# import datetime
#
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d"))


# --- circle area---
# radius = float(input("what the radius of the circle? : "))
# p = 3.14
# result = p * (radius ** 2)
# print("Area: ", result)


# first_name = input("first name: ")
# last_name = input("last name")
# full_name_rev = last_name + " " + first_name
# print("Full Name\n" + full_name_rev.capitalize())

# array
# num = input("Enter numbers: ")
# list = num.split(",")
# tuple = tuple(list)
#
# print(list)
# print(tuple)


# file name  extension

# file = input("file name: ")
# c = 0
# for i in file:
#     if i != ".":
#         c += 1
#     else:
#         break
# extension = file[c + 1:]
# print(extension)

# color_list = ["Red","Green","White" ,"Black"]
# print("first color: ", color_list[0],
#       "\nlast color: ", color_list[-1])

# exam_st_date = (11, 12, 2014)
# txt = "The examination will start from : {}/{}/{} "
# print(txt.format(exam_st_date[0], exam_st_date[1], exam_st_date[2]))


# n = int(input("Enter number: "))
# result = n + (n*11) + (n*111)
# print("sum =", result)

# func= input("Enter function name:")
#
# print(func.__doc__)


# import calendar
# y = int(input("Enter year: "))
# m = int(input("Enter month: "))
# print(calendar.month(y, m))


# print("""In this format of 3 quotation marks
# you can skip lines and still get your-------->
# <-----------string printed ------------------->
#           '         -        '
#             '       -      '
#                '    -    '
#                  '  -  '
#                    '-'
# """)


# from datetime import date
# dt_1 = date(2022,3,12)
# dt_2 = date(2021, 12, 19)
#
# dif = dt_1 - dt_2
# print(dif.days)


# n = int(input("Enter a number: "))
# if n > 17:
#     print(abs(n - 17)*2)
# else:
#     print(abs(17 - n))

# n = int(input("Enter a number: "))
# if abs(n - 1000) < 100 or abs(n - 2000) < 100:
#     print(n, "num is in range")
# else:
#     print(n, "not in range of thousand")


# def sum_or_treepile(a, b, c):
#     if a == b and a == c:
#         return (a + b + c) * 3
#     else:
#         return a + b + c
#
#
# print(sum_or_treepile(5, 5, 5))


# def Is_in_str(txt):
#     if "Is" not in txt[0] + txt[1]:
#         txt = "Is " + txt
#         return  txt
#     else:
#         return txt
# print(Is_in_str("out Is the door"))

# def str_dubbeld(str, n):
#     return str * n
# print(str_dubbeld("str", 4))

# n = int(input("Enter a number: "))
# if n %2 == 0:
#     print(n ,"is even number")
# else:
#     print(n, "is odd number")

# def count_4(l):
#     c = l.count(4)
#     return c
# l = [3,4,5,6,3,4,9]
# print(count_4(l))

# def n_copies_2(txt, n):
#     if len(txt) < 2:
#         return txt * n
#     else:
#         return txt[:2] * n
#
# text = "Im very happy with my team proformnce"
# print(n_copies_2(text,6))


# def vowels_in_char(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(vowels_in_char("w"))
#
#
# def fide_value(list,value):
#     return value in list
# l = [12,2,3,4,5,6,7,8,9,0]
# print(fide_value(l, 12))


# def histogram(list):
#     carecter = "*"
#     for i in list:
#         print(carecter * i)
# print(histogram([3,9,6,1]))

# def re_srt(list):
#     st= ""
#     for i in range(len(list)):
#         st = st + str(list[i])
#     return st
#
# l = [3,4,7,90,4,]
# print(re_srt(l))

#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
# for i in numbers:
#     if (i % 2 == 0) and i != 237:
#         print(i)
#     elif i == 237:
#         print(i)
#         break


# def colors_lists(list_1, list_2):
#     match = []
#     for x in list_1:
#         if x not in list_2:
#             match.append(x)
#     return match
#
#
# color_list_1 = ["White", "Black", "Red","Green", "Blue"]
# color_list_2 = ["Red", "Green", "Black"]
# print(colors_lists(color_list_1, color_list_2))


# def triangle_area(b, h):
#     return (b * h) // 2
# print(triangle_area(12,14))
#
#
# count_pair = 0
# count_dev_4 = 0
# for i in range(1,52):
#     if i % 2 == 0:
#         count_pair +=1
#         if i % 4 == 0:
#             count_dev_4 +=1
# print("number of pair: ", count_pair)
# print("number devaid by 4: ", count_dev_4)

#
# l = [1, 1]
#
# for i in range(40):
#     l.append(l[i] + l[i + 1])
#
# print("index 42 equals =", l[41])
#
# n_1 = 1
# n_2 = 1
#
# for i in range(20):
#     n_1 = n_1 + n_2
#     n_2 = n_1 + n_2
#
# print(n_2)
#
# def train_work_ap(age, height, name):
#     if age < 18:
#         return "To young"
#     elif height != 156:
#         return "Wrong height"
#     elif name[0] not in ("a", "b"):
#         return "Name not good"
#     else:
#         return "you are accepted"
#
#
# print(train_work_ap(19, 156, "bele"))
#
#
# num = 52
# while num >=23:
#     print(num)
#     num -=1

# num = 100
# while num <= 250:
#     if num % 2 != 0:
#         print(num)
#     num += 1


# import random
#
# num = random.randrange(1,100)
# count_pair = 0
# count_div6 = 0
# count_bigger_50 = 0
# total = 0
#
# while num != 7:
#     if num % 2 == 0:
#         count_pair +=1
#     if num % 6 == 0:
#         count_div6 +=1
#     if num > 50:
#         count_bigger_50 +=1
#     total +=1
#     num = random.randrange(1,100)
# print("pair count =",count_pair)
# print("divided by 6 count =",count_div6)
# print("bigger then 50 count",count_bigger_50)
# print("total intersessions=",total)
# print("num is", num)


# num = int(input("Enter number: "))
# count_pair = 0
# count_div6 = 0
# count_bigger_50 = 0
# total = 1
# while num != 7:
#
#     if num % 2 == 0:
#         count_pair +=1
#     if num % 6 == 0:
#         count_div6 +=1
#     if num > 50:
#         count_bigger_50 +=1
#     total +=1
#     num = int(input("Enter number: "))
# print("pair count =",count_pair)
# print("divided by 6 count =",count_div6)
# print("bigger then 50 count",count_bigger_50)
# print("total intersessions=",total)
# print("num is", num)
#
# n_1 = int(input("Enter number: "))
# n_2 = int(input("Enter number: "))
# n_3 = int(input("Enter number: "))
# n_4 = int(input("Enter number: "))
# n_5 = int(input("Enter number: "))
# n_6 = int(input("Enter number: "))
# c = 0
# c_b5 = 0
# max = n_1
# min = n_1
# for i in (n_1, n_2, n_3, n_4, n_5, n_6):
#     if max < i:
#         max = i
#     if min > i:
#         min = i
#     if i > 5:
#         c_b5 +=1
#     if i % 2 == 0:
#         c += 1
# print("max num=", max)
# print("min num=", min)
# print("above 5 count=", c_b5)
# print("even nums count=", c)
#
#


# def all_pairs(n):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(i, j)
#
#
# def all_pairs_sum(m, n):
#     # Write your solution here
#     sum = 0
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             sum += (i * j)
#     return sum


# def print_rectangle(height, width):
#     # Write your solution here
#     for h in range(height):
#         for w in range(width):
#             print("#", end=" ")
#         print("")

# print(all_pairs_sum(2, 3))


# l = []
# for i in range(4):
#     str = input("say something: ")
#     l.append(str)
# print(len(l))
# print((l))
# l.insert(1, "cr7")
# print(l)
# print(l[2])
# l.remove(l[0])
# sort = sorted(l)
# print(sort)
#


# import time
# x = time.time()
# sum([1]*1000000)
# y = time.time()
# print("measured time", y-x)
#
# ls1 = [1, 4, 7]
# ls2 = [2, 5, 8]
# ls3 = [3, 6, 9]
# ls4 = [ls1, ls2, ls3]
# for i in range(len(ls4)):
#     for j in range(len(ls4[i])):
#         print(ls4[i][j], end=" ")
#     print("")

#
# def avg_grade(lst):
#     # delete pass and fill in your code below
#     l = []
#     for i in lst:
#         if i >= 60:
#             l.append(i)
#     return sum(l) / len(l)


# ls1 = ["yosi", "vala","dor"]
# ls2 = []
# for i in range(len(ls1)):
#     if 'o' in ls1[i]:
#         ls2.append(ls1[i])
# print(ls2)

# t1 = ("a", "w", "t", "f", "q")
# t2 = ("f", "m", "c", "r", "s")
# print(t1)
# print(t2)
# print(t1[3])
# print(t2[3])
# print(t1[2:4])
# print(t2[2:4])
# lst = ["done", (1, 3, 7), "now"]
# print(lst)
# lst.remove(lst[1])
# print(lst)

# check if list is sorted ot not
# def is_sorted(lst):
#     # delete pass and fill in your code below
#     for i in range(len(lst)-2):
#         if lst[i] > lst[i+1]:
#             return False
#     return True

# find k number in a given list
# def kth_element(lst, k):
#     # delete pass and fill in your code below
#     for i in range(k):
#         minmum = min(lst)
#         lst.remove(minmum)
#
#     return minmum


# checks if string hold two same characters following each
# def twice(st):
#     # delete pass and fill in your code below
#     for i in range(1,len(st)):
#         if st[i] == st[i-1]:
#             return True
#     return False
# l = [4,5,6,7,8,1,9]
# print(twice(l))

# filter negative numbers from list
# def filter_negative(L):
#     # delete pass and fill in your code below
#     positive_l = []
#     for i in L:
#         if i > 0:
#             positive_l.append(i)
#     return positive_l


# -----------------------------------------------------------------------------------------------------------------------------------

# 1LCM -- lowest common multiple
#
# def lcm(a,b):
#     c = max(a, b)
#     while True:
#         if (c % a == 0) and (c % b == 0):
#             lcm = c
#             break
#
#         else:
#             c +=1
#     return lcm
#
# print((lcm(17,15)))


#  sum of three given integers
# def sum_3(x, y , z):
#     if x != y and x!= z and y != z:
#         return f"sum = {(x + y + z)}"
#     else:
#         return "sum = 0"
#
# print(sum_3(0,4,7))


# sum of two given integers
# def sum_2(x,y):
#     res = x + y
#     if 14 < res <= 20:
#         return "sum = 20"
#     else:
#         return f"sum = {res}"
# print(sum_2(9,80))


# return true if the two given integer values
# def If_True(x,y):
#     return x == y or x + y == 5 or abs(x - y) == 5
# print(If_True(4,1))

# program to add two objects if both objects are an integer type

# def Is_int(x,y):
#     if type(x) == int and type(y) == int:
#         return x+y
#     else:
#         return "not integer"
#
# print(Is_int(3,"5"))

#  Python program to display your details like name, age, address in three different lines

# def tree_lins(str):
#     str= str.split(",")
#     for i in range(len(str)):
#         print(str[i])
# a = "yalem bakala,age 27 ,add: brzil 100//55"
# print(tree_lins(a))

#  Python program to solve (x + y) * (x + y)
# def upper_by_sum(a,b):
#     return (a+b)*(a+b)
# print(upper_by_sum(3,4))

# Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
# def ribit(amt, tasoa,years):
#     tasoa = tasoa / 100
#     for i in range(years):
#         amt = amt + (amt * tasoa)
#     return f"After {years} with int of {tasoa} per year\nAmt will be worth {round(amt,2)}"
# print(ribit(10000, 3.5, 7))

#  Python program to compute the distance between the points (x1, y1) and (x2, y2)
# import math
# def Distance(p1, p2):
#
#     d1 = abs(p1[0] - p2[0])**2
#     d2 = abs(p1[1] - p2[1])**2
#     distance = math.sqrt(d1 + d2)
#     return f"Distance = {round(distance,4)}"
#
#
# print(Distance([22,0], [45,6]))


# import os.path
# print(os.path.exists('test.txt'))


# # For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)

# import platform
# import os
# print("Name of the operating system:",os.name)
# print("\nName of the OS system:",platform.system())
# print("\nVersion of the operating system:",platform.release())
#
# import site;
# print(site.getsitepackages())

# import os
# print("Current File Name : ",os.path.realpath(__file__))
#
# import multiprocessing
# print(multiprocessing.cpu_count())


# for i in range(0, 10):
#     print('*', end="")
# print("")
