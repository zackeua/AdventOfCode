import sys
# requires python 3.10 for pattern matching

def print_grid(grid):
    for row in grid:
        print(''.join(['#' if elem == 1 else '.' for elem in row]))
    print()
    

with open(sys.argv[1], 'r') as f:
    data = [row.split() for row in f.readlines()]

grid_width = 50
grid_height = 6
grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
temp_grid = [[0 for _ in range(grid_height)] for _ in range(grid_width)]

for row in data:
    match row:
        case ['rect', _]:
            width, height = list(map(int, row[1].split('x')))
            for h in range(height):
                for w in range(width):
                    grid[h][w] = 1
        case ['rotate', 'column', *rest]:
            for h in range(grid_height):
                for w in range(grid_width):
                    temp_grid[w][h] = grid[h][w]
            
            COLUMN = int(row[2][2:])
            shift_amount = int(row[-1])
            temp_grid[COLUMN] = temp_grid[COLUMN][-shift_amount:] + temp_grid[COLUMN][:-shift_amount]

            for h in range(grid_height):
                for w in range(grid_width):
                    grid[h][w] = temp_grid[w][h]
            
        case ['rotate', 'row', *rest]:
            ROW = int(row[2][2:])
            shift_amount = int(row[-1])
            grid[ROW] = grid[ROW][-shift_amount:] + grid[ROW][:-shift_amount]

print_grid(grid)

print(sum([sum(row) for row in grid]))
