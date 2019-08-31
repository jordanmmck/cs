n = int(input())
nums = input().split()
nums = list(map(int, nums))
t = tuple(nums)

print(hash(t))
