S = input()

alphanum = alpha = digits = lower = upper = False

for c in S:
    if c.isalnum():
        alphanum = True
    if c.isalpha():
        alpha = True
    if c.isdigit():
        digits = True
    if c.islower():
        lower = True
    if c.isupper():
        upper = True

print(alphanum)
print(alpha)
print(digits)
print(lower)
print(upper)
