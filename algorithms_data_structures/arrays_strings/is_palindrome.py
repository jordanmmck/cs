# is a string a palindrome


def is_pal(s):
    if len(s) <= 1:
        return True

    i, j = 0, len(s) - 1

    while i < j:
        i += 1
        j -= 1
        if s[i] != s[j]:
            return False

    return True


hello = 'helloworld'
print(hello)
print(is_pal(hello))

racecar = 'racecar'
print(racecar)
print(is_pal(racecar))
