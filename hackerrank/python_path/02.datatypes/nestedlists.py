N = int(input())
L = []
scores = set()

for i in range(N):
    name = input()
    grade = float(input())
    L.append([name, grade])
    scores.add(grade)
# print(L)

scorelist = sorted(scores)

# print(scorelist)
secondlow = scorelist[1]

# print(secondlow)

people = []
for i in range(N):
    if L[i][1] == secondlow:
        people.append(L[i][0])

# print(people)
people.sort()
for p in people:
    print(p)
