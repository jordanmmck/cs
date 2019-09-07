from collections import deque

T = int(input())
for i in range(T):
    n = int(input())
    d = deque()
    l = []
    d.extend(list(map(int, input().split())))

    for j in range(n):

        if d[0] >= d[-1]:
            if len(l) == 0:
                l.append(d.popleft())
                continue
            elif d[0] > l[-1]:
                print('No')
                # print(d)
                # print(l)
                break
            l.append(d.popleft())
        elif d[0] < d[-1]:
            if len(l) == 0:
                l.append(d.pop())
                continue
            if d[-1] > l[-1]:
                print('No')
                # print(d)
                # print(l)
                break
            l.append(d.pop())
    # print(len(d))
    if len(d) == 0:
        print('Yes')
