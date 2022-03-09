#is_palindrome function#

def is_palindrome(st):
    # delete pass and fill in your code below
    l = 0
    r = len(st) - 1
    while r > l:
        if st[l] != st[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_palindrome("elijle"))



#space count function

s = (input("white something"))
c = 0
for char in s:
    if char == " ":
        c +=1
print(c)

#char count function
s = input("white something ")
c = input("witch char to count?" )
count = 0
for char in s:
    if char == c:
        count +=1
print(count)

# average function
exam = int(input("Exam grade: "))

hw = int(input("hw grade: "))

if exam >= 60 and abs exam - hw < 25:
        print (round((exam * 0.75) + (hw * 0.25)))
else:
     print(exam)


# # pass or fail function
grade = int(input("Enter Grade: "))
if (grade >= 60) and (grade <= 100):
    print("pass")
elif grade >= 0 and grade < 60:
    print("fail")
else:
    print("invalid")



#bith-date guusing function
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

