# L = []
# for i in range(1,10+1):
#     L = L + [i]
# print(L)

# import random
# L2 = []
# for i in range(10):
#     L2 = L2 + [random.randrange(1,100)]
# print("Random List L2: ",L2)
# L3 = []
# for i in range(len(L2)):
#     minmum = min(L2)
#     L2.remove(minmum)
#     L3. append(minmum)
#
# print("Sorted List L3: ", L3)
#

# l = []
# while len(l) < 11:
#     n = int(input("Enter a number: "))
#     if n > 0:
#         l.append(n)
#     else:
#         n = int(input("Enter a positive number: "))
# print(l)
# l = [11, 3, 44, 81, 21, 9, 70, 60, 45, 12, 43]
#
# print("sum", sum(l))
# print("Division  by 11:")
# for i in l:
#     print(i / 11)
# print("count bigger then 10: ")
# count = 0
# for i in l:
#     if i >= 10:
#         count += 1
# print(count)
# print("count less then 10:")
# print(len(l)-count)
# print("max number in the list: ",max(l))
# print("even numbers: ")
# for i in l:
#     if i % 2 == 0:
#         print(i, end=" ")
# print("")
# print("Divided by 3:")
# for i in l:
#     if i % 3 == 0:
#         print(i, end=" ")
#
# l = [11, 3, 44, 81, 20, 21, 70, 60, 61, 12, 43]
#
# for i in range(1, len(l)):
#     if l[i] == l[i - 1]:
#         print("Their match values", l[i], "and", l[i - 1])
#         break
# else:
#     print("The list don't contain same following numbers")
# print("insert 3 to index[0]")
# l.insert(0,3)
# print(l)
# user_num = int(input("Enter a number: "))
# print("insert user_num to index [1]")
# l.insert(1, user_num)
# print(l)
# print("insert sum(l[0]+l[1] to index [2]")
# res = l[0]+l[1]
# l.insert(2, res)
# print(l)
# print("insert multi(l[0]*l[1]*l[2]) to index [3]")
# res1 = l[0]*l[1]*l[2]
# l.insert(3, res1)
# print(l)
# for i in l:
#     print(i, end=",")
#
#
# l1 = []
# l2 = []
# for i in range(2):
#     for j in range(5):
#         if len(l1) != 5:
#             grade1 = int(input("Enter grade stud-1:"))
#             l1.append(grade1)
#             continue
#         grade2 = int(input("Enter grade stud-2:"))
#         l2.append(grade2)

l2 = [90, 89, 89, 97, 78]
l1 = [77, 33, 33, 33, 2]
# for i in l1:
#     if i in l2:
#         print("The students have at list one matching grade")
#
#         break
#     else:
#         print("The students don't have matching grades")
#         break

#
# def same_grade(l1,l2):
#     for i in l1:
#         if i in l2:
#             print("The students have at list one matching grade")
#             return True
#
#
#         else:
#             print("The students don't have matching grades")
#             return False
#
# print((same_grade(l1,l2)))

# st = input("Say something:\n")
# n = len(st)
# if n % 2 == 0:
#     print("len str in even", n)
# else:
#     print("len str not even number", n)

# s = 0
# l_10 = []
#
# for i in range(3):
#     st = input("road:")
#     dis = int(input("distance"))
#     s = s + dis
#     if dis > 10:
#         l_10.append(st)
#
# print("total distance:", s)
# #
# print("roads longer then 10k:")
# print(l_10)
# p = 35
# d = 10
# minmum = 4
# count_20 = 0
# for i in range(2):
#     name = input("company name:")
#     ord_c = int(input("amount ordered:"))
#     payment = p * ord_c
#     if ord_c < minmum:
#         payment += d
#     print("company name:", name)
#     print("payment:",payment)

#     if ord_c > 20:
#         count_20 += 1
# print("Amount of companies\nThat ordered above\n20 boxes:", count_20)


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#     "electric": False,
#   "year": 1964,
#     "color": ["black", "white", "red"]
#
#
# }
# print(type(thisdict))


# l = []
# for i in range(2):
#     family = input("family:")
#     num_kids = int(input("number of kids:"))
#     tuple = (family, num_kids)
#     l.append(tuple)
# s = 0
# for i in range(len(l)):
#     s = s + l[i][1]
#     if l[i][1] > 3:
#         print(l[i][0], " family get discount")
# print("amount of kids going to the trip:", s, "kids")
# l = []
# l2 = []
# l3 = []
#
# doneters = {"name": l,
#             "b_date": l2,
#             "type": l3
#             }
# count_o = 0
#
# for j in range(25):
#             n = input("name: ")
#             l.append(n)
#             d = int(input("birth-date: "))
#             l2.append(d)
#             t = input("type: ")
#             l3.append(t)
#             if t == "o":
#                 count_o += 1
# print(doneters["type"])
# print("type O count =", count_o)





# for  i in range(5):