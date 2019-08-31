l = [(3, 'c'), (3, 'c'), (3, 'b'), (3, 'a'), (4, 'z'), (1, 'x')]

# s=sorted(unsorted, key=lambda element: (element[1], element[2]))
# print(s)

# l = [['name_d', 5], ['name_e', 10], ['name_a', 5]]
l_sorted = sorted(l, key=lambda x: (x[1] * -1, x[0]))
l.sort(key=lambda x: (x[1] * -1, x[0]))

print(l)
print(l_sorted)
