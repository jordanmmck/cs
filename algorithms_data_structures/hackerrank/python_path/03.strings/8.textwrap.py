import textwrap

S = input()
w = int(input())

# print(textwrap.wrap(S,w))
print(textwrap.fill(S, w))
