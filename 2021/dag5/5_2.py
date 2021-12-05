import sys

with open(sys.argv[1], 'r') as f:
    coords = [[list(map(int, elems.split(',')))
               for elems in line.split(' -> ')] for line in f.readlines()]
print(coords)

mininum = min([min([min(coord) for coord in row]) for row in coords])
maximum = max([max([max(coord) for coord in row]) for row in coords])+1

grid = [[0]*(maximum - mininum) for _ in range(maximum-mininum)]

for row in coords:
    if row[0][0] == row[1][0] or row[0][1] == row[1][1]:
        #print(row)
        loopx = range(
            row[0][0], row[1][0]+1) if row[0][0] < row[1][0] else range(row[1][0], row[0][0]+1)
        loopy = range(
            row[0][1], row[1][1]+1) if row[0][1] < row[1][1] else range(row[1][1], row[0][1]+1)
        for x in loopx:
            for y in loopy:
                #print(x, y)
                grid[y-mininum][x-mininum] += 1

    
    if row[0][0] < row[1][0]:
        if row[0][0] - row[1][0] == row[0][1] - row[1][1]:
            #print(row)
            looplen = row[1][0] - row[0][0] + 1
            beginx = row[0][0]
            beginy = row[0][1]
            for i in range(looplen):
                #print(beginx + i, beginy + i)
                grid[beginy+i-mininum][beginx+i-mininum] += 1
        elif row[0][0] - row[1][0] == row[1][1] - row[0][1]:
            #print(row)
            looplen = row[1][0] - row[0][0] + 1
            beginx = row[0][0]
            beginy = row[0][1]
            for i in range(looplen):
                #print(beginx + i, beginy - i)
                grid[beginy-i-mininum][beginx+i-mininum] += 1

    else:
        if row[1][0] - row[0][0] == row[0][1] - row[1][1]:
            #print(row)
            looplen = row[0][0] - row[1][0] + 1
            beginx = row[0][0]
            beginy = row[0][1]
            for i in range(looplen):
                #print(beginx - i, beginy + i)
                grid[beginy+i-mininum][beginx-i-mininum] += 1

        elif row[1][0] - row[0][0] == row[1][1] - row[0][1]:
            #print(row)
            looplen = row[0][0] - row[1][0] + 1
            beginx = row[0][0]
            beginy = row[0][1]
            for i in range(looplen):
                #print(beginx - i, beginy - i)
                grid[beginy-i-mininum][beginx-i-mininum] += 1



'''
for row in grid:
    for elem in row:
        print('.' if elem==0 else elem, end='')
    print()
'''
count = sum([sum([elem >= 2 for elem in row]) for row in grid])
print(count)
