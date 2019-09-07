N = int(input())
A = list(map(int, input().split()))
l = sorted(set(A))
if len(l) > 1:
    print(l[-2])
