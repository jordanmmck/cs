import itertools


def f(x):
    return x**2


# K lists and M is the mod
K, M = map(int, input().split())

masterlist = []
listlens = []

for i in range(K):
    inp = list(map(int, input().split()))
    N = inp[0]
    listlens.append(N)
    l = inp[1:]
    masterlist.append(l)

maxval = 0
for i in itertools.product(*masterlist):
    l = list(i)
    val = 0
    for x in l:
        val += f(x)
    val = val % M
    if val > maxval:
        maxval = val

print(maxval)
