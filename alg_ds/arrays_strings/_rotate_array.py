# given a list rotate it left n places
# [1,2,3], 1 => [2,3,1]
# [1,2,3], 2 => [3,1,2]

# 1. Calculate the shift = (size - num_rotations) % size
# 2. Make new array T
# 3. T[(i+shift)%size]=A[i]

# runtime: O(n)
# space: O(n)

# 1. Store num_rotations elements in temp array
# 2. Shift other elements
# 3. append temp array to original

# runtime: O(n)
# space: O(num_rotations)


def rot(arr):
    return None


l = [1, 2, 3, 4, 5, 6]
print(l)
print(rot(l))
