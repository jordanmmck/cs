from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

for tup in list(product(A, B)):
    print(tup, end=' ')
