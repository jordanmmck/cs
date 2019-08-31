S = input()
length = len(S)
vowels = ['A', 'E', 'I', 'O', 'U']
k = s = 0

for i in range(length):
    # print(S[i:])
    if S[i] in vowels:
        k += length - i
    else:
        s += length - i

if k == s:
    print('Draw')
elif k > s:
    print('Kevin' + ' ' + str(k))
else:
    print('Stuart' + ' ' + str(s))
