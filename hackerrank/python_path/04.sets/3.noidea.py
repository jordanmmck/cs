n, m = map(int, input().split())

# n ints in arr
arr = list(map(int, input().split()))

# both are size m
# like A, dislike B
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happy = 0

for i in arr:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
print(happy)
