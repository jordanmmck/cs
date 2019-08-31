S = input()
N = ''

for c in S:
    if 64 < ord(c) < 91:
        N = N + chr(ord(c) + 32)
    elif 96 < ord(c) < 123:
        N = N + chr(ord(c) - 32)
    else:
        N = N + c

print(N)
