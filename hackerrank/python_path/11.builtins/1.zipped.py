# l1=[1,2,3]
# l2=['a','b','c']
# print(list(zip(l1,l2)))

# A=[1,2]
# B=[3,4]
# C=[5,6]
# X=[A]+[B]+[C]
# print(list(zip(*X)))

N, X = map(int, input().split())
masterlist = []
for i in range(X):
    marks = list(map(float, input().split()))
    masterlist.append(marks)

l = list(zip(*masterlist))
for s in l:
    total = sum(s)
    print(total / X)
