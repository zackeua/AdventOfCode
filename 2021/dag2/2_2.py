import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()

dist = 0
aim = 0
depth = 0
for op in data:
        code, val = op.split(' ')
        if code == 'forward':
                dist += int(val)
                depth += aim * int(val)
        elif code == 'down':
                aim += int(val)
        else:
                aim -= int(val)
print(dist*depth)
