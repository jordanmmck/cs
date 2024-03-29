# map
from functools import reduce
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

# filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
