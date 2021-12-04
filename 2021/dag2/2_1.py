import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()

dist = 0
depth = 0
for op in data:
        code, val = op.split(' ')
        if code == 'forward':
                dist += int(val)
        elif code == 'down':
                depth += int(val)
        else:
                depth -= int(val)
print(dist*depth)