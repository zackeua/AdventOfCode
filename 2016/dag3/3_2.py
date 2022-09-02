from calendar import c
import sys

def is_triangle(l):
    if l[0] + l[1] <= l[2]:
        return False
    if l[1] + l[2] <= l[0]:
        return False
    if l[0] + l[2] <= l[1]:
        return False
    
    return True


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [list(map(int, row.split())) for row in data]

for i in range(0, len(data), 3):
    data[i][1], data[i+1][0] = data[i+1][0], data[i][1]
    data[i][2], data[i+2][0] = data[i+2][0], data[i][2]
    data[i+1][2], data[i+2][1] = data[i+2][1], data[i+1][2]



print(sum([is_triangle(tripple) for tripple in data]))