from itertools import combinations_with_replacement

S = input().split()
k = int(S[1])
S = S[0]

l = list(combinations_with_replacement(S, k))
for i, tup in enumerate(l):
    subl = sorted(tup)
    l[i] = ''.join(subl)
l.sort()

for x in l:
    print(x)
