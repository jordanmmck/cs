# given a list reverse it


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
