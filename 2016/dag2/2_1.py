import sys

def move(pos, s):
    if s == '':
        return pos
    
    next_pos = {('1', 'R'): '2', ('1', 'D'): '4',
                ('3', 'L'): '2', ('3', 'D'): '6',
                ('7', 'R'): '8', ('7', 'U'): '4',
                ('9', 'L'): '8', ('9', 'U'): '6',
                ('2', 'R'): '3', ('2', 'L'): '1', ('2', 'D'): '5',
                ('8', 'R'): '9', ('8', 'L'): '7', ('8', 'U'): '5',
                ('4', 'D'): '7', ('4', 'U'): '1', ('4', 'R'): '5',
                ('6', 'D'): '9', ('6', 'U'): '3', ('6', 'L'): '5',
                ('5', 'R'): '6', ('5', 'L'): '4', ('5', 'U'): '2', ('5', 'D'): '8'}

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