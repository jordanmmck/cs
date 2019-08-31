def ransom_note(magazine, ransom, m, n):
    d = {}
    t = {}
    for word in magazine:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    for word in ransom:
        if word not in d:
            return False
        elif d[word] < 1:
            return False
        else:
            d[word] -= 1
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom, m, n)
if(answer):
    print("Yes")
else:
    print("No")
