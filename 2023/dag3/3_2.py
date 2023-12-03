import sys


def is_num(c):
    return c in '0123456789'

def is_symbol(c):
    return not is_num(c) and c != '.' 

def search_left(row, col, grid):
    total = 0
    base = 1
    for i, elem in enumerate(grid[row][0:col][::-1]):
        if is_num(elem):
            total += int(elem) * base
            base *= 10
            #grid[row][col-i-1] = '_'
        else:
            break
    return total

def search_right(row, col, grid, start=0):
    total = start

    for i, elem in enumerate(grid[row][col+1:]):
        if is_num(elem):
            total *= 10
            total += int(elem)
            #grid[row][col+i+1] = '_'
        else:
            break
    return total

def search_above(row, col, grid):
    if row-1 < 0:
        return 0, 0
    
    #print(grid[row-1][col])
    if is_num(grid[row-1][col]):
        tmp = search_left(row-1, col, grid)
        total1 = search_right(row-1, col-1, grid, tmp)
        total2 = 0
    else:
        total1 = search_left(row-1, col, grid)
        total2 = search_right(row-1, col, grid)

    return total1, total2

def search_below(row, col, grid):
    if row+1 >= len(grid):
        return 0, 0
    total1, total2 = search_above(row+2, col, grid)
    return total1, total2


def search(grid):
    total = 0
    for row, line in enumerate(grid):
        for col, elem in enumerate(line):
            gear_ratio = 1
            if elem == '*':
                left = search_left(row, col, grid)
                right = search_right(row, col, grid)
                above_left, above_right = search_above(row, col, grid)
                below_left, below_right = search_below(row, col, grid)
                cond = 0
                for elem in [left, right, above_left, above_right, below_left, below_right]:
                    if elem != 0:
                        gear_ratio *= elem
                    cond += elem != 0
                    
                if cond == 2:
                    total += gear_ratio

    return total


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[c for c in line] for line in data]
        total = search(data)
        print(total)
if __name__ == '__main__':
    main()