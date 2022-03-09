is_palindrome function#

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


