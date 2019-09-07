n = int(input())
eng = set(map(int, input().split()))

b = int(input())
fre = set(map(int, input().split()))

print(len(eng.difference(fre)))
