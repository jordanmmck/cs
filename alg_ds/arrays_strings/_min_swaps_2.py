# https://www.hackerrank.com/challenges/minimum-swaps-2

# i   arr                         swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]

# 5 swaps


def min_swaps(arr):
    val_to_ind = {}
    for i, x in enumerate(arr):
        val_to_ind[x] = i

    count = 0
    for i, x in enumerate(arr):

        if i + 1 != x:
            ind = val_to_ind[i + 1]
            arr[i] ^= arr[ind]
            arr[ind] ^= arr[i]
            arr[i] ^= arr[ind]
            val_to_ind[x] = ind
            count += 1

    return count


arr = [7, 1, 3, 2, 4, 5, 6]
print(arr)
print(min_swaps(arr))
