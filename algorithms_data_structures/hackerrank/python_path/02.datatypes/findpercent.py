N = int(input())

names = []
marks = []
for i in range(N):
    line = input().split()
    name = line[0]
    names.append(name)
    mark = [float(line[1]), float(line[2]), float(line[3])]
    marks.append(mark)

name = input()
index = names.index(name)
print("%.2f" % (sum(marks[index]) / 3))
