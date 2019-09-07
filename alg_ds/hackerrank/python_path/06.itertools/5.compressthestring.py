from itertools import groupby

groups = []
uniquekeys = []

data = list(input())
for k, g in groupby(data):
    groups.append(list(g))
    uniquekeys.append(k)

for i, l in enumerate(groups):
    tup = (len(l), int(l[0]))
    print(tup, end=' ')
