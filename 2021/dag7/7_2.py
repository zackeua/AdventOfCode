
import sys

def sum_int(val):
    return val*(val+1)//2

with open(sys.argv[1], 'r') as f:
    pos = list(map(int, f.readline().split(',')))

align_cost = [sum([sum_int(abs(pos[i] - j)) for i in range(len(pos))])
              for j in range(max(pos))]

#print(align_cost)

print(min(align_cost))
