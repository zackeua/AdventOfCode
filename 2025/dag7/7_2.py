import sys
from collections import defaultdict
from functools import lru_cache

global grid


@lru_cache()
def search(start: complex, depth: int):
    global grid
    direction = 1j
    next_position = start + direction
    if next_position.imag >= depth:
        return 1
    if grid[next_position] == "^":
        grid[next_position - 1] = "|"
        grid[next_position + 1] = "|"
        return search(next_position - 1, depth) + search(next_position + 1, depth)
    else:
        grid[next_position] = "|"
        return search(next_position, depth)


def main():
    global grid
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        # print(data)

    grid = defaultdict(lambda: ".")
    start = None
    for row_i, row in enumerate(data):
        for col_i, elem in enumerate(row):
            position = col_i + row_i * 1j
            if elem == "S":
                start = position
            grid[position] = elem

    total = search(start, len(data))
    # for row_i, row in enumerate(data):
    # for col_i, elem in enumerate(row):
    # position = col_i + row_i * 1j
    # print(grid[position], end="")
    # print()
    print(total)


if __name__ == "__main__":
    main()
