def array_left_rotation(L, num_ints, num_rots):
    shift = (num_ints - num_rots) % num_ints
    temp = 0
    pos = 0
    for i in range(num_ints):
        temp = L[(pos + shift) % num_ints]
        L[(pos + shift) % num_ints] = L[pos]
        pos = (pos + shift) % num_ints
    return L


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
