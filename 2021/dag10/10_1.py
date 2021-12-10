import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [[elem for elem in row if elem != '\n'] for row in data]

d = {')': 0, ']': 0, '}': 0, '>': 0}

for row in data:
    stack = []
    for c in row:
        if c in '([{<':
            stack.append(c)

        elif len(stack) > 0:
            if stack[-1] == '(' and c == ')':
                stack = stack[:-1]
            elif stack[-1] == '[' and c == ']':
                stack = stack[:-1]
            elif stack[-1] == '{' and c == '}':
                stack = stack[:-1]
            elif stack[-1] == '<' and c == '>':
                stack = stack[:-1]
            else:
                d[c] += 1
                break
print(d[')']*3+d[']']*57+d['}']*1197+d['>']*25137)
