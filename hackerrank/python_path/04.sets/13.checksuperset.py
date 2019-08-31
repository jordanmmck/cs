A = set(input().split())
N = int(input())
out = True
for i in range(N):
    B = set(input().split())
    if len(B.difference(A)) != 0 or len(A.difference(B)) == 0:
        out = False
print(out)
