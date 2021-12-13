import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]

def fold(coords, dir, pos):
    new_coords = []
    if dir == 'y':
        for elem in coords:
            if elem[1] < pos and elem not in new_coords:
                new_coords.append(elem)
            elif elem[1] > pos and (elem[0], 2*pos - elem[1]) not in new_coords:
                new_coords.append((elem[0], 2*pos - elem[1]))
    if dir == 'x':
        for elem in coords:
            if elem[0] < pos and elem not in new_coords:
                new_coords.append(elem)
            elif elem[0] > pos and (2*pos - elem[0], elem[1]) not in new_coords:
                new_coords.append((2*pos - elem[0], elem[1]))
    return new_coords

def min_coord(coords):
    min_x = min([elem[0] for elem in coords])
    min_y = min([elem[1] for elem in coords])
    return min_x, min_y

def max_coord(coords):
    max_x = max([elem[0] for elem in coords])
    max_y = max([elem[1] for elem in coords])
    return max_x, max_y

def disp(coords):
    min_x, min_y = min_coord(coords)
    max_x, max_y = max_coord(coords)

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            print('#' if (x,y) in coords else '.', end = '')
        print()




coords = []
ops = []
index = len(data)
for i, row in enumerate(data):
    if row == '':
        index = i
    if i < index:
        coords.append(tuple(list(map(int, row.split(',')))))
    if i > index:
        a, b, c = row.split(' ')
        a, b = c.split('=')
        ops.append((a, int(b)))


for op in ops:
    coords = fold(coords, op[0], op[1])

disp(coords)
