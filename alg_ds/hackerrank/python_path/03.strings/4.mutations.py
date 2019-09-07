string = input()
line = input().split()
index = int(line[0])
char = line[1]

l = list(string)
l[index] = char
string = ''.join(l)
print(string)
