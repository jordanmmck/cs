n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    oper = input().split()
    s = set(map(int, input().split()))
    if oper[0] == 'intersection_update':
        A.intersection_update(s)
    elif oper[0] == 'difference_update':
        A.difference_update(s)
    elif oper[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(s)
    elif oper[0] == 'update':
        A.update(s)

print(sum(A))
