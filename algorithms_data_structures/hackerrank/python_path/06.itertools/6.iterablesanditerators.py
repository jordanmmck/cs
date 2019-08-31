from itertools import combinations

N = int(input())
l = list(input().split())
K = int(input())

lcomb = list(combinations(l, K))
count = 0
for tup in lcomb:
    if 'a' in tup:
        count += 1
prob = count / len(lcomb)
print(prob)
