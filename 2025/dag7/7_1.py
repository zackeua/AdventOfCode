import sys
from collections import defaultdict


def search(
    grid: defaultdict[complex],
    start: complex,
    depth: int,
    split_grid: defaultdict[complex],
):
    direction = 1j
    next_position = start + direction
    if grid[next_position] == "|":
        return split_grid
    if next_position.imag >= depth:
        return split_grid
    if grid[next_position] == "^":
        split_grid[next_position] = 1
        search(grid, next_position - 1, depth, split_grid)
        search(grid, next_position + 1, depth, split_grid)
        return split_grid
    else:
        grid[next_position] = "|"
        return search(grid, next_position, depth, split_grid)


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        # print(data)

    grid = defaultdict(lambda: ".")
    split_grid = defaultdict(lambda: 0)
    start = None
    for row_i, row in enumerate(data):
        for col_i, elem in enumerate(row):
            position = col_i + row_i * 1j
            if elem == "S":
                start = position
            grid[position] = elem

    split_grid = search(grid, start, len(data), split_grid)
    total = 0
    for row_i, row in enumerate(data):
        for col_i, elem in enumerate(row):
            position = col_i + row_i * 1j
            total += split_grid[position]
            # print(grid[position], end="")
        # print()
    print(total)


if __name__ == "__main__":
    main()
