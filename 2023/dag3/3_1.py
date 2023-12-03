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
            grid[row][col-i-1] = '_'
        else:
            break
    return total

def search_right(row, col, grid, start=0):
    total = start

    for i, elem in enumerate(grid[row][col+1:]):
        if is_num(elem):
            total *= 10
            total += int(elem)
            grid[row][col+i+1] = '_'
        else:
            break
    return total

def search_above(row, col, grid):
    if row-1 < 0:
        return 0
    
    total = 0
    #print(grid[row-1][col])
    if is_num(grid[row-1][col]):
        tmp = search_left(row-1, col, grid)
        total += search_right(row-1, col-1, grid, tmp)
        #print(grid[row-1][col-1:])
    else:
        total += search_left(row-1, col, grid)
        total += search_right(row-1, col, grid)

    return total

def search_below(row, col, grid):
    if row+1 >= len(grid):
        return 0
    return search_above(row+2, col, grid)


def search(grid):
    total = 0
    for row, line in enumerate(grid):
        for col, elem in enumerate(line):
            if is_symbol(elem):
                total += search_left(row, col, grid)
                total += search_right(row, col, grid)
                total += search_above(row, col, grid)
                total += search_below(row, col, grid)
    #print(grid)
    
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