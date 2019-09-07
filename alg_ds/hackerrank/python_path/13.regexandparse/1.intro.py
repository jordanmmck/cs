# >>> import re
# >>> print bool(re.search(r"ly","similarly"))
# True
import re

R = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')

T = int(input())
for i in range(T):
    x = input()
    print(bool(R.match(x)))
