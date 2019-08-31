S = list(input())
prev = ''
S[0] = S[0].upper()
for i, c in enumerate(S):
    if prev == ' ':
        S[i] = c.upper()
    prev = c
print(''.join(S))
