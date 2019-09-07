N, M = map(int, input().split())
table = []
for i in range(N):
    l = list(map(int, input().split()))
    table = table + [l]

K = int(input())
table.sort(key=lambda x: int(x[K]))

for x in table:
    print(*x, sep=' ')
