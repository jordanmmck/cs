import re

T = int(input())
for i in range(T):
    S = input()
    try:
        a = re.compile(S)
        print('True')
    except Exception:
        print('False')
