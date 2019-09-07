# ascii 97 = a
# ascii 98 = b
# ...

N = int(input())

width = (N * 2 - 1) * 2 - 1
c = 96 + N

for x in range(N):
    s = ''
    for i in range(x + 1):
        s = s + chr(c - i) + '-'
    for j in range(x - 1, -1, -1):
        s = s + chr(c - j) + '-'
    s = s[:-1]
    print(s.center(width, '-'))
for x in range(N - 1, 0, -1):
    s = ''
    for i in range(x):
        s = s + chr(c - i) + '-'
    for j in range(x - 2, -1, -1):
        s = s + chr(c - j) + '-'
    s = s[:-1]
    print(s.center(width, '-'))
