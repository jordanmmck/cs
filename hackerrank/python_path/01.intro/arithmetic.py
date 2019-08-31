# read 2 ints

# read in a big string
nums = input()

# split by spaces, save as a list
nums = nums.split()

# convert from list of strings to list of ints
nums = list(map(int, nums))
print(nums)

a, b = nums[0], nums[1]

# print sum
print(a + b)

# print diff (first-sec)
print(a - b)

# print prod
print(a * b)
