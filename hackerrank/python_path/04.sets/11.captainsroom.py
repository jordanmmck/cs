K = int(input())
l = list(map(int, input().split()))

length = len(l)
if K % 2 == 0:
    curr = l[0]
    for i in range(1, length):
        curr ^= l[i]
    print(curr)
else:
    l.sort()
    prev = l[0]
    count = 1
    for i in range(1, length):
        curr = l[i]
        count += 1
        if i == length - 1:
            print(curr)
            break
        if l[i] != prev:
            if count != K + 1:
                print(prev)
                break
            count = 1
        prev = l[i]
