# def notGetNotReturnFunc():
#     print(("hi from notGetNotReturnFunc"))
# def GetAndNotReturn(x):
#     print(x)
# def NotGetAndReturnFunc():
#     return "hi from notGetNotReturnFunc"
# def GetAndReturnFunc(x,y):
#     return x*y
#
# notGetNotReturnFunc()
# GetAndNotReturn(7)
# print(NotGetAndReturnFunc())
# print(GetAndReturnFunc(7, 4))
#
# 1
# x = int(input("enter number"))
# def even_num(n):
#     if n % 2 == 0:
#         return 0
#     else:
#         return 1
# print(even_num(x))


# 2
# def avg(n):
#     c = 0
#     for i in range(n):
#         x = int(input("enter num: "))
#         c +=x
#     res = c/n
#     return "Average = " + str(res)
# print(avg(4))


# 3
# def len_num():
#     n = input("Enter num: ")
#     while not n.isnumeric():
#         n = input("Enter number: ")
#     return len(n)
# print(len_num())


# 4
# def change(n):
#     x = n // 20
#     res = n - (20*x)
#     y = res // 10
#     res = n - ((20*x) + (10*y))
#     z = res // 5
#     o = n - ((20*x) + (10*y) + (5*z))
#     txt = "change contin:\n{} of 2os,\n{} of 10s,\n{} of 5s,\nand {} ones"
#     return txt.format(x, y, z, o)
# res = change(89)
# print(res)

# 5
# def pow(x,y):
#     res = 1
#     for i in range(y):
#       res *=x
#     return res
# print(pow(2,4))

# def aks_dis():
#     dis = int(input("discount: "))
#     return dis
#
# #6
# def price(n):
#     if n > 1000:
#         d = aks_dis()
#         res = n * (d/100)
#         return n - res
#     else:
#         res = n * 0.10
#         return n - res
# print(price(1100))


# 7
# def Quadratic(a,b,c):
#     res1= 0
#     res2 = 0
#     if a != 0:
#         mona = (b**2) - (4*a*c)
#         if mona < 0:
#             return "negative number"
#         for i in range(mona//2):
#             if i * i == mona:
#                 mona = i
#                 break
#     else:
#         return "a = 0"
#     res1= (-b + mona) // 2*a
#     res2= (-b - mona) // 2*a
#     return res1, res2
#
# print(Quadratic(1,12,16))


# 9

# def math(x, y):
#     import math
#     result = input(""""
#     a-the biggest devider
#     b-the smallest divider
#     c-the result of pow(a,b)
#     d-the result of sqrt(a)-sqrt(b)]
#     e-exi
#     choice: """)
#     while result != "e":
#         if result == "a":
#             if x % y == 0:
#                 return x
#             else:
#                 for i in range(x , 0, -1):
#                     if y % i == 0:
#                         return i
#         elif result == "b":
#                 for i in range(2,x // 2):
#                     if y % i == 0:
#                         return i
#         elif result == "c":
#             res = 1
#             for i in range(y):
#                 res *= x
#             return res
#         elif result == "d":
#             res1= math.sqrt(x)
#             res2= math.sqrt(y)
#             return res1 -res2
#
#         break
# print(math(20,16))

# def loopList(x):
#     for i in range(x):
#         yield i
# print(list(loopList(5)))


# def name(s):
#     print("hello "+s)
# print(name("yalem"))

# def sum_numbers(x,y):
#     print(x+y)
# print(sum_numbers(5,4))
#
# def sum_numbers(x,y):
#     return x + y
# print(sum_numbers(5,4))

# def loop(n):
#     for i in range(n):
#         yield i
# print(list(loop(6)))

# def re_loop(n):
#     for i in range(n,0,-1):
#         yield i
# print(list(re_loop(6)))


# def p_list(ls, x):
#     ls.sort(reverse=x)
#     print(ls)
# ls = [3,1,4]
# p_list(ls, True)
