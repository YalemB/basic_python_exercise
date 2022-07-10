# check ID validation digit

ID = input("Enter 8 id digits: ")
while not ID.isnumeric() or len(ID) != 8:
    ID = input("Invalid digits\nEnter 8 id digits: ")


def check_digit(id):
    x = 0
    res = 0

    for i in range(len(id)):
        # 1,3,5,7
        if i % 2 != 0:
            x = (int(id[i]) * 2)
        else:
            x = (int(id[i]))
        if x < 10:
            res = res + x
        else:
            res = res + ((x % 10) + (x // 10))
    digit = 10 - (res % 10)
    if digit != 10:
        return "check_digit = " + str(digit)
    else:
        return "check_digit = " + "0"

st = "23240884"
print(check_digit(ID))
# def caesar_encrypt(k, txt):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     cipher = ""
#     for char in txt:
#         if char in alphabet:
#             place = alphabet.find(char)
#             new_place = (place + k) % 26
#             cipher += alphabet[new_place]
#         else:
#             cipher += char
#     return cipher
#
#
# x = caesar_encrypt(5, "ronaldo the king")
# print(x)
#
#
# def caesar_decrypt(k, txt):
#     text = caesar_encrypt(-k, txt)
#     return text






# # o = "jxu gkuijyed ev mxujxuh q secfkjuh sqd jxyda yi de cehu ydjuhuijydw jxqd jxu gkuijyed ev mxujxuh q ikrcqhydu sqd imyc"
# #
# #
# # def caesar_break(st):
# #     for offset in range(1, 26):
# #         maybe = caesar_decrypt(offset, st)
# #         print(offset, "-------->", maybe)
# #
# # caesar_break(o)

# # def code(msg,alphabet,shuffled):
# #     cipher = ""
# #     for char in msg:
# #         if char in alphabet:
# #             p = shuffled.find(char)
# #             o = alphabet[p]
# #             cipher += o
# #         else:
# #             cipher += char
# #     return cipher
# # alphabet = "abcdefghijklmnopqrstuvwxyz"
# # shuffled = "pqmxayjwgcnirzsevuoldfkhbt"
# # x= "qazzb"
# # print(code(x,alphabet,shuffled))


# def char_count(text):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     A01 = []
#     A02 = []
#     for char in alphabet:
#         how_many = text.count(char)
#         if how_many > 0:
#             percent = (how_many * 100) / len(text)
#             A01.append(percent)
#             A02.append(char)
#             x = A01.index(max(A01))
#             del A01[x]
#             del A02[x]
#             x = A01.index(max(A01))
#             return (A02[x], "frequency:", A01[x], "%")


# # print(char_count())

# z="most paragraphs in an essay parallel the general three-part" 
# print(char_count(z))


