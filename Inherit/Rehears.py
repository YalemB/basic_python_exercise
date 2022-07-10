
# s = "MDCXCV"
#
# def romanToInt(s: str):
#     numbers = 0
#     romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     for i in range(len(s)):
#         if len(s) > i+ 1 and romans[s[i]] < romans[s[i+1]]:
#             numbers -= romans[s[i]]
#         else:
#             numbers += romans[s[i]]
#     return numbers

# def romanToInt(s: str):
#     numbers = 0
#     romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     odds = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
#     n = len(s)
#     i = 0
#     while n > i:
#         if len(s) > 1 and s[i:i + 2] in odds.keys():
#             numbers += odds[s[i:i + 2]]
#             i += 2
#         else:
#             numbers += romans[s[i]]
#             i += 1
#
#     return numbers


# def romanToInt(s: str):
#     numbers = 0
#     romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     odds = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
#     n = len(s)
#     i = 0
#     while n > i:
#
#         if n - i == 1:
#             r = s[i]
#             o = s[i]
#         else:
#             o = s[i] + s[i + 1]
#             r = s[i]
#         if o in (odds.keys()):
#             i += 2
#             numbers += odds[o]
#
#         elif r in (romans.keys()):
#             numbers += romans[r]
#             i += 1
#     return numbers

#
# print(romanToInt(s))
# strs = ["flower","flow","flight"]
#
# def longestCommonPrefix(strs):
#     match = ""
#     n = len(strs)
#     # go throw the whole list strings
#     for i in range(n):
#         # Find the character you are comparing
#         x = strs[0][i]
#         for j in range(n):
#             #comparation with the other first words
#             if x != strs[j][i]:
#                 return match
#         # if all the letters match add to match string
#         match+= x
#     return match
#
# longestCommonPrefix(strs)



# s3 = "(([]){})"
#
#
# def isValid(s):
#     n = len(s)
#     if n % 2 != 0:
#         return False
#
#     left = ["(", "{", "["]
#     right = [")", "}", "]"]
#     add = []
#     l = 0
#     r = 0
#
#     for j in range(n):
#         char = s[j]
#         if char in (left):
#             l += 1
#             add.append(char)
#             continue
#         elif char in (right) and len(add) > 0:
#
#             char_befor_left = add[-1]
#             if char == ")" and char_befor_left == "(" or char == "]" and char_befor_left == "[" or char == "}" and char_befor_left == "{":
#                 r += 1
#                 add.pop(-1)
#
#                 continue
#             else:
#                 return False
#         else:
#             return False
#
#     return l == r
#
#
# print(isValid(s3))







list1 = [1,2,4]
list2 = [1,3,4]
Output = [1,1,2,3,4,4]


# def mergeTwoLists(list1, list2):
#     n = min(len(list1) , len(list2))
#     m = max(len(list1) , len(list2))
#     z = m - n
#     if len(list1) > len(list2):
#         long_list = list1
#     else:
#         long_list = list2
#     new_list =[]
#     for i in range(n):
#         l1 = list1[i]
#         l2 = list2[i]
#         if l1 < l2:
#             new_list = new_list+ [l1] + [l2]
#
#         else:
#             new_list = new_list + [l2] + [l1]
#     if z != 0:
#         return new_list + long_list[z:]
#     else:
#         return new_list
#
# res = mergeTwoLists(list1,list2)
# print(res)
# print(res == Output)
l = [0,0,1,1,1,2,2,3,3,5,4,7,7,8,3,4]

def removeDuplicates(nums):
    new_list = []

    for i in nums:
        if nums.count(i) == 1 or i not in(new_list):
            new_list.append(i)
    res = len(nums) - len(new_list)
    return new_list + [""]* res, res




print(removeDuplicates(l))
print(len(l))