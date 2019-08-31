def number_needed(a, b):
    A = [0] * 26
    B = [0] * 26
    for c in a:
        A[ord(c) - 97] += 1
    for c in b:
        B[ord(c) - 97] += 1
    sum_diff = 0
    for i in range(26):
        sum_diff += abs(A[i] - B[i])

    return sum_diff


a = input().strip()
b = input().strip()

print(number_needed(a, b))
