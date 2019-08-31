string = input()
sub = input()

i = 0
count = 0
while True:
    i = string.find(sub, i)
    if i == -1:
        break
    i += 1
    count += 1

print(count)
