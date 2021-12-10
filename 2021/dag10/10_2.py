import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [[elem for elem in row if elem != '\n'] for row in data]

def score(l_list):
    score = 0
    d = {')': 1, ']': 2, '}': 3, '>': 4}
    for elem in l_list:
        score *= 5
        score += d[elem]
    return score



add = False
stacks = []

pam = {'(': ')', '[': ']', '{': '}', '<': '>'}

for row in data:
    if add:
        stacks.append([pam[elem] for elem in stack[::-1]])
    
    add = True
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
                add = False
                break

if add:
    stacks.append([pam[elem] for elem in stack[::-1]])

scores = list(map(score, stacks))
scores.sort()

print(scores[len(scores)//2])
