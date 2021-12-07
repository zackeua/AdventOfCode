import sys

with open(sys.argv[1], 'r') as f:
    pos = list(map(int, f.readline().split(',')))

align_cost = [sum([abs(pos[i] - j) for i in range(len(pos))]) for j in range(max(pos))]

print(min(align_cost))
