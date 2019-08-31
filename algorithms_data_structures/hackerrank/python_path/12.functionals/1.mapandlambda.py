def fib(n):
    if n == 0:
        return 0
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


N = int(input())

l0 = [fib(i) for i in range(N)]
l1 = list(map(lambda x: x**3, l0))
print(l1)
