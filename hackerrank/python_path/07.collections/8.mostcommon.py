# aabbbccde
# b 3
# a 2
# c 2
from collections import Counter

S = list(input())
d = Counter(S)

l = [(v, k) for v, k in d.items()]

# l_sorted = sorted(l, key=lambda x: (x[1] * -1, x[0]))
l.sort(key=lambda x: (x[1] * -1, x[0]))
print(l)

final = l[0:3]
for x in final:
    print(x[0] + ' ' + str(x[1]))
