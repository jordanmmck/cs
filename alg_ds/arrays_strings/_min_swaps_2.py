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
    return 0


arr = [7, 1, 3, 2, 4, 5, 6]
print(arr)
print(min_swaps(arr))

# At every step it should become more ordered, never less
# so a search would terminate. Hill climb?
# from 2 to 6 are in order, these are not candidates to swap
# you want the best bang for your buck
# you want the swap that will move the big value farthest right
# and the small val farthest left
# can you not just look at the diff between the value and the normalized index?
# find the largest and smallest in one pass
# still n^2
