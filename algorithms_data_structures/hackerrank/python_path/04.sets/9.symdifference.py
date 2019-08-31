n = int(input())
eng = set(map(int, input().split()))

b = int(input())
fre = set(map(int, input().split()))

inter = eng.union(fre)
s = eng.intersection(fre)
print(len(inter.difference(s)))
