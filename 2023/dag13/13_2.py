import sys


def find_col_reflections(grid: list[str]):
    for i in range(len(grid)):
        offset = i+1
        upper = grid[:offset]
        length = min(2*offset, len(grid))
        lower = grid[offset:length]
        if len(upper) < len(lower):
            lower = lower[::-1]
        else:
            upper = upper[::-1]
        # print('Lower: ', lower)
        # print('Upper: ', upper)
        matching = len(lower) and len(upper)
        for u, l in zip(upper, lower):
            if u != l:
                matching = False
        if matching:
            return len(upper)
    return None


def flip_axes(grid):
    data = []

    for x in zip(*grid):
        data.append(''.join(x))
    return data


def find_row_reflections(grid: list[str]):
    data = flip_axes(grid)
    cols = find_col_reflections(data)
    return cols


def find_reflections(data: list[str]):
    mapping = {'.': '#', '#': '.'}
    old_rows = find_row_reflections(data)
    old_cols = find_col_reflections(data)
    print('Old:', old_cols, old_rows)
    for r, row in enumerate(data):
        for c, elem in enumerate(row):
            grid = data.copy()
            grid[r] = row[:c] + mapping[elem] + row[c+1:]
            assert len(grid[r]) == len(data[r])
            # print(data)
            # print(grid)
            rows = find_row_reflections(grid)
            cols = find_col_reflections(grid)
            if rows == old_rows and cols == old_cols:
                continue

            if rows is not None or cols is not None:
                print('New: ', cols, rows)
                if cols is None or cols == len(data) or cols == old_cols:
                    cols = 0
                if rows is None or rows == len(data[0]) or rows == old_rows:
                    rows = 0
                return cols, rows
    return cols or 0, rows or 0

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
            # for line in grid:
            #    # print(line)
            print(cols, rows, len(grid), len(grid[0]))
            total += cols*100 + rows
        print(total)
        assert total != 17076
        assert total > 15318
        assert total > 5370


if __name__ == '__main__':
    main()
