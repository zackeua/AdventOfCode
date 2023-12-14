import sys


def find_col_reflections(grid: list[str], old=-1):
    for i in range(len(grid)-1):
        offset = i+1
        upper = grid[:offset]
        lower = grid[offset:2*offset]
        if len(upper) < len(lower):
            lower = lower[::-1]
        else:
            upper = upper[::-1]
        # print('Lower: ', lower)
        # print('Upper: ', upper)
        matching = len(lower) > 0 and len(upper) > 0
        for u, l in zip(upper, lower):
            if u != l:
                matching = False
                break
        if matching and len(upper) != old:
            return len(upper)
    # print('No match')
    return None


def flip_axes(grid):
    data = []

    for x in zip(*grid):
        data.append(''.join(x))
    return data


def find_row_reflections(grid: list[str], old=-1):
    data = flip_axes(grid)
    cols = find_col_reflections(data, old)
    return cols


def find_reflections(data: list[str]):
    mapping = {'.': '#', '#': '.'}
    old_rows = find_row_reflections(data)
    old_cols = find_col_reflections(data)
    # print('Old:', old_cols, old_rows)
    for r, row in enumerate(data):
        for c, elem in enumerate(row):
            grid = data.copy()
            grid[r] = row[:c] + mapping[elem] + row[c+1:]
            assert len(grid[r]) == len(data[r])
            # print(data)
            # print(grid)
            rows = find_row_reflections(grid, old_rows)
            cols = find_col_reflections(grid, old_cols)

            if rows is not None or cols is not None:
                #for p in grid:
                #    print(p)
                #print('New: ', cols, rows)
                return cols, rows, old_cols, old_rows
    return cols, rows, old_cols, old_rows

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
            cols, rows, old_cols, old_rows = find_reflections(grid)
            # for line in grid:
            #    # print(line)
            cols = cols or 0
            rows = rows or 0
            # print(cols, rows, old_cols, old_rows, len(grid), len(grid[0]))
            total += cols*100 + rows
        print(total)
        assert total != 17076
        assert total > 15318
        assert total > 5370


if __name__ == '__main__':
    main()
