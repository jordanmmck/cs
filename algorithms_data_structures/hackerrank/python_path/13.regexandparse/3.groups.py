# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.group(0)       # The entire match
# 'username@hackerrank.com'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'username'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'hackerrank'
# >>> m.group(3)       # The third parenthesized subgroup.
# 'com'
# >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
# ('username', 'hackerrank', 'com')
import re

S = input()
print(re.search(r'(\w{2,})', S))
