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
#
# def til_q():
#     l = []
#     # first input from user
#     n = (input("Enter number:\nOr quit 'q'"))
#     try:
#         while n != "q":
#             # add n lo List
#             l.append(int(n))
#             # Get new numbers from user
#             n = (input("Enter number: \n Or quit 'q'"))
#
#         # When input n == "q"
#         return "Average=" + str(sum(l) / len(l))
#
#     except ValueError :
#         print("try again!")
#
# print(til_q())
#
# def get_odd_numbers():
#    numbers = [n for n in range(10)]
#
#    odd_numbers = []
#    for i in numbers:
#        if i % 2 == 1:
#            number = numbers.pop(i)
#            odd_numbers.append(number)
#            print(odd_numbers)
#
#    return odd_numbers

# print(get_odd_numbers())


# s = "A man, a plan, a canal: Panama"
# s2 = "race a car"
#
# def is_palindrum(st):
#     st = st.casefold()
#     new_st = ""
#     for char in st:
#         if char.isalnum():
#             new_st = new_st + char
#     rev = new_st[::-1]
#
#     return new_st == rev
#
# print(is_palindrum(s))


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



# def twoSum( nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(1+i,n):
#             total = nums[i] + nums[j]       # sum i + j
#             if total == target:
#                 return "indexes = {},{}".format(i,j)
#
#
# nums = [3,3,2]
#
# target = 5


# print(twoSum(nums,target))

# indexes = [i for i, x in enumerate(nums)]
# list1 = [i for i in nums]
# for i in nums:
#     for j, s in zip(nums, indexes):
#         if i == j and nums.index(i) == s:
#             pass
#         elif i + j == target:
#             return [nums.index(i), s]

# print(twoSum(nums,target))


#
# def addTwoNumbers(l1,l2):
#     st = ""
#     st_2 = ""
#     for i in range(len(l1),0,-1):
#         st += str(l1[i-1])
#
#     for j in range(len(l2),0,-1):
#         st_2 += str(l2[j-1])
#     return int(st) + int(st_2)
# def addTwoNumbers(l1,l2):
#     num1 = ""
#     num2 = ""
#     x = l1[::-1]
#     y = l2[::-1]
#     for i in(y):
#         num1+= str(i)
#     for j in (x):
#         num2 += str(j)
#
#     return int(num1) + int(num2)

# def addTwoNumbers(l1,l2):
#     num1 = ""
#     num2 = ""
#     for i in range(len(l1)):
#         num1 += str(l1[-1])
#         l1.remove(l1[-1])
#
#     for j in range(len(l2)):
#         num2 += str(l2[-1])
#         l2.remove(l2[-1])
#     print(num1,num2)
#     return int(num1) + int(num2)


# res = addTwoNumbers([2,4,3],[5,6,4])
# print(res)




# def count_evens(nums):
#   c = 0
#   for i in nums:
#     x = i
#     if x % 2:
#       c+=1
#   return c
#
#
# res = count_evens([2, 1, 2, 3, 4])
#
# print(res)

#
# def count_code(str):
#     count = 0
#     i = 0
#     while i < len(str):
#         check = str[i:i+4]
#         if check[:2] == "co" and check[-1] == "e":
#             count += 1
#             i +=3
#         i+=1
#
#
#     return count
#
# print(count_code('cozexxcope'))

corts = ["rhal","daniya","pilip"]

choise = input("choose cort: rhal/daniya/pilip")

def form():
    players_list = []
    players = 0
    while players< 2:
        player_name = input("Enter name: ")
        phone_num = input("Enter number: ")
        while not phone_num.isnumeric() or len(phone_num) != 10 or phone_num[:2] != "05":
            phone_num = input("Invalid number\nTry again!: ")
        players += 1
        info = {"player": player_name, "phone_number": phone_num,"id":players}
        players_list.append(info)

    print("There enough players to play")
    print(f"place: {choise}")
    print("players")
    print(players_list)

form()


