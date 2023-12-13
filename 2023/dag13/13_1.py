import sys


def find_col_reflections(grid: list[str]):
    for i in range(len(grid)):
        offset = i+1
        upper = grid[:offset]
        lower = grid[offset:2*offset]
        if len(upper) < len(lower):
            lower = lower[::-1]
        else:
            upper = upper[::-1]
        matching = True
        for u, l in zip(upper, lower):
            if u != l:
                matching = False
        if matching:
            return len(upper)


def flip_axes(grid):
    data = []

    for x in zip(*grid):
        data.append(''.join(x))
    return data


def find_row_reflections(grid: list[str]):
    data = flip_axes(grid)
    cols = find_col_reflections(data)
    return cols


def find_reflections(grid: list[str]):
    rows = find_row_reflections(grid)
    cols = find_col_reflections(grid)
    if cols == len(grid):
        cols = 0
    if rows == len(grid[0]):
        rows = 0
    return cols, rows


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

        all_grids = []
        grid = []
        for line in data:
            if line != '':
                grid.append(line)

            if line == '':
                all_grids.append(grid)
                grid = []
        all_grids.append(grid)

        total = 0
        for grid in all_grids:
            cols, rows = find_reflections(grid)
            print(cols, rows, len(grid), len(grid[0]))
            total += cols*100 + rows
        print(total)


if __name__ == '__main__':
    main()
