import cmath as cm
import re

comp = input()
l = re.findall(r'[-]?\d+', comp)

x = y = 1
x, y = map(int, l)

r = cm.phase(complex(x, y))
theta = abs(complex(x, y))

print(theta)
print(r)
