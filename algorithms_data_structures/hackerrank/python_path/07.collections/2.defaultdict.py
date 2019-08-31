from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)
# print(d)

n, m = map(int, input().split())

# group A
A = []
for i in range(n):
    A.append(input())

# group B
B = defaultdict(list)
for i, x in enumerate(A):
    B[x].append(i + 1)

for i in range(m):
    word = input()
    if word in B:
        l = B[word]
        for c in l:
            print(c, end=' ')
        print('')
    else:
        print(-1)
