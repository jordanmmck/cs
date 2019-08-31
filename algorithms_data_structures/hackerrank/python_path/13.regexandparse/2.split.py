# >>> import re
# >>> re.split("-","+91-011-2711-1111")
# ['+91', '011', '2711', '1111']

import re

# print(*re.split("[.,]",input()),sep='\n')
l = re.split("[.,]", input())
l1 = filter(None, l)
print(*l1, sep='\n')
