# given a list reverse it

# 1. Two pointers, one at start, one at end
# 2. Swap values of element at each pointer
# 3. Increment one, decrement other
# 4. Reapeat as long as i<j


def rev(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        # fancy bit manip swap
        arr[i] ^= arr[j]
        arr[j] ^= arr[i]
        arr[i] ^= arr[j]
        i += 1
        j -= 1

    return arr


l = [1, 2, 3, 4, 5, 7]
print(l)
print(rev(l))
