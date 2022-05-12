# import datetime
#
# x = datetime.datetime.now()
# y = x.year
# day = x.strftime("%A")
# # print(x)
# # print(y)
# # print(day)
# # crateing date
# birth_date = datetime.datetime(1994,10,15)
# print(x.strftime("%b"))
# print(birth_date.strftime("%d"))
import json
# #jason format text
# x = '{ "name":"yalem", "age":27, "city":"jerusalem"}'
#
# y = json.loads(x)
#
# ls_keys = list(y.keys())
# ls_values = list(y.values())
# print(ls_values)
# print(ls_keys)
# import json
#
# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])


# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x, indent= 4, separators=(","," is "))
#
# # the result is a JSON string:
#
# p
# rint(y)


# #bith-date guusing function
import random
day = int(input("Enter day of birth: "))
while day > 31:
    print("Day out of range enter valid day")
    day = int(input("Enter a other day : "))

month = int(input("Enter month of birth: "))
while month > 12:
    print("Month out of range enter valid month")
    month = int(input("Enter a other month : "))


d = random.randrange(1,31)
m = random.randrange(1,13)
count = 1
while day != d or month != m:
    d = random.randrange(1, 31+1)
    m = random.randrange(1, 12+1)

    count += 1
txt ="It took {} irritations to get this date {}/{}"
print(txt.format(count,day,month))

