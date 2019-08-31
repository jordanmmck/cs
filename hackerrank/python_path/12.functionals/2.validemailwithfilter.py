import re


def m(s):
    R = re.compile(r'^[a-z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')
    if(R.match(s)):
        return True
    else:
        return False

# s1='harsh@gmail'
# s2='iota_98@hackerrank.com'

# print(m(s1))
# print(m(s2))


N = int(input())
l = []
for i in range(N):
    l.append(input())

l1 = sorted(filter(m, l))
print(l1)
