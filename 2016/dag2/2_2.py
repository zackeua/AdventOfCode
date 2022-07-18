import sys

def move(pos, s):
    if s == '':
        return pos

    next_pos = {('1', 'D'): '3',
                ('5', 'R'): '6',
                ('9', 'L'): '8',
                ('D', 'U'): 'B',
                ('2', 'R'): '3', ('2', 'D'): '6',
                ('4', 'L'): '3', ('4', 'D'): '8',
                ('A', 'R'): 'B', ('A', 'U'): '6',
                ('C', 'L'): 'B', ('C', 'U'): '8',
                ('3', 'U'): '1', ('3', 'R'): '4', ('3', 'D'): '7', ('3', 'L'): '2',
                ('6', 'U'): '2', ('6', 'R'): '7', ('6', 'D'): 'A', ('6', 'L'): '5',
                ('7', 'U'): '3', ('7', 'R'): '8', ('7', 'D'): 'B', ('7', 'L'): '6',
                ('8', 'U'): '4', ('8', 'R'): '9', ('8', 'D'): 'C', ('8', 'L'): '7',
                ('B', 'U'): '7', ('B', 'R'): 'C', ('B', 'D'): 'D', ('B', 'L'): 'A'}

    if (pos, s[0]) in next_pos:
        pos = next_pos[(pos, s[0])]
    
    return move(pos, s[1:])

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.strip() for row in data]
    print(data)

code = ''
prev = '5'
for row in data:
    prev = move(prev, row)
    code += prev

print(code)