#1

# def til_q():
#     l = []
#     # first input from user
#     n = (input("Enter number:\nOr quit 'q'"))
#
#     while n != "q":
#         # add n lo List
#         l.append(int(n))
#         # Get new numbers from user
#         n = (input("Enter number: \n Or quit 'q'"))
#
#     # When input n == "q"
#     return "Average=" + str(sum(l) / len(l))
# print(til_q())

#2

# def is_palidum(st):
#     s = 0
#     e = len(st)-1
#     while e >= s:
#         if st[s] != st[e]:
#             return False
#         s += 1
#         e -= 1
#     return True
# txt = "adc !cda"
# print(is_palidum(txt))

#3

# def postive_nums(ls):
#     for i in range(len(ls)):
#         if ls[i] < 0:
#             return False
#     return True
#
# l= [2,5,-9,12,0,77,5]
# print(postive_nums(l))

#4

# def min_hour(n):
#     x = n / 60
#     txt ="{} minutes equal {} hours"
#     return txt.format(n,round(x,2))
# print(min_hour(68))

#5

# def is_True(a,b):
#     if a == b:
#         return True
#     else:
#         return False
# x= 5 < 2
# y = 10  < 11
# print(is_True(x,y))

#6
# def count_l(L):
#     new_l =[]
#     for i in range(10):
#         c = L.count(i)
#         new_l.append(c)
#     return new_l
#
# l = [8,6,5,3,5,0,9,8,1,2,3,6,7,8,3,4,5,0,1,9,2,8,3,8,3,7,4,6,5,6,9,9,9]
# print(count_l(l))


# def sum_nums(x,y):
#     return x + y
# def multi_nums(x,y):
#     return x * y
# def sum_n_multi(x,y):
#    return  sum_nums(x,y), multi_nums(x,y)
# print(sum_n_multi(5,8))

# def xyz_there(str):
#   n = len(str)
#   for i in range(n-2):
#     d = str[i-1]
#     c = str[i] + str[i+1] + str[i+2]
#     if c == "xyz" and d != ".":
#       return True
#   return False

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True


# def big_diff(nums):
#   maximum = nums[0]
#   minmum = nums[0]
#   for i in range(len(nums)):
#     if nums[i] > maximum:
#       maximum = nums[i]
#     if nums[i] < minmum:
#       minmum = nums[i]
#   return maximum - minmum
#
#
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

#
# def centered_average(nums):
#   maximum = nums[0]
#   minmum = nums[0]
#   for i in range(len(nums)):
#     if nums[i] > maximum:
#       maximum = nums[i]
#     if nums[i] < minmum:
#       minmum = nums[i]
#   nums.remove(maximum)
#   nums.remove(minmum)
#   return int(sum(nums) / len(nums))
#
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3



