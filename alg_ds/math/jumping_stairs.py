def get_min_stair_jumps(n, s):
    count = 0
    i = 0

    while(True):
        if i == n - 1:
            print(i)
            return count
        count += 1
        next = s[i + 1]
        if next == 1:
            i += 2
            continue
        if next == 0 and n - i == 2:
            i += 1
            continue
        nextnext = s[i + 2]
        if next == 0 and nextnext == 0:
            i += 2
            continue
        if next == 0 and nextnext == 1:
            i += 1
            continue


get_min_stair_jumps(6, [0, 0, 1, 0, 1, 0])
