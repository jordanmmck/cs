M = input()
s1 = set(map(int, input().split()))

N = input()
s2 = set(map(int, input().split()))

# union = s1.union(s2)
# inter = s1.intersection(s2)
diff1 = s1.difference(s2)
diff2 = s2.difference(s1)
symdiff = diff1.union(diff2)

# print(union)
# print(inter)
# print(diff1)
# print(diff2)
# print(symdiff)
l = sorted(symdiff)

for i in l:
    print(i)
