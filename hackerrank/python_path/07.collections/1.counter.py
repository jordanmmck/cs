from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print(Counter(myList))
# #Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

# print(Counter(myList).items())
# #[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

# print(Counter(myList).keys())
# #[1, 2, 3, 4, 5]

# print(Counter(myList).values())
# #[3, 4, 4, 2, 1]

X = int(input())
sizes = list(map(int, input().split()))
inventory = Counter(sizes)
profit = 0

for i in range(int(input())):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        profit += price
        inventory[size] -= 1
print(profit)
