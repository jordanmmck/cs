from itertools import combinations

S = input().split()
k = int(S[1])
S = S[0]

for i in range(1, k + 1):
    l = list(combinations(S, i))
    for i, tup in enumerate(l):
        subl = sorted(tup)
        l[i] = ''.join(subl)
    l.sort()
    for x in l:
        print(x)

    # for j,sub in enumerate(l):
    # 	subl = list(sub).sort()
    # 	subl=''.join(subl)
    # 	l[j]=subl
    # l.sort()
    # print(l)
