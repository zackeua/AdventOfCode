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

print(sum([is_triangle(tripple) for tripple in data]))