from itertools import permutations

S = input().split()
num = int(S[1])
S = S[0]

l = list(permutations(S, num))
for i, x in enumerate(l):
    l[i] = ''.join(x)

l.sort()
for string in l:
    print(string)
