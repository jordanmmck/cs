def is_matched(expression):
    l = []
    for char in expression:
        if char == '{':
            l.append('{')
        elif char == '[':
            l.append('[')
        elif char == '(':
            l.append('(')
        elif not l:
            return False
        elif char == '}':
            if l.pop() != '{':
                return False
        elif char == ']':
            if l.pop() != '[':
                return False
        elif char == ')':
            if l.pop() != '(':
                return False
    return True


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
