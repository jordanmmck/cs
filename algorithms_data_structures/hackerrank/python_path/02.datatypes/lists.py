L = []
N = int(input())

for i in range(N):

    string = input().split()

    if string[0] == 'insert':
        L.insert(int(string[1]), int(string[2]))
    elif string[0] == 'print':
        print(L)
    elif string[0] == 'remove':
        L.remove(int(string[1]))
    elif string[0] == 'append':
        L.append(int(string[1]))
    elif string[0] == 'sort':
        L.sort()
    elif string[0] == 'pop':
        L.pop()
    elif string[0] == 'reverse':
        L.reverse()
