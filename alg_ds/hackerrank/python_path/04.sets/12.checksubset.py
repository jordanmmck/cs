# More than 4 lines will result in 0 score. Blank ln n counted.
for i in range(int(input())):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(not bool(len(A.difference(B))))
