import textwrap
from collections import OrderedDict
S = input()
N = len(S)
K = int(input())

strings = textwrap.wrap(S, K)
for i, string in enumerate(strings):
    strings[i] = ''.join(OrderedDict.fromkeys(strings[i]))
for word in strings:
    print(word)
