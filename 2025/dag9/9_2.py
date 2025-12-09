import sys
import itertools
import collections


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [tuple(map(int, line.split(","))) for line in data]
        # print(data)
    largest_area = 0
    min_x = sys.float_info.max
    min_y = sys.float_info.max
    max_x = sys.float_info.min
    max_y = sys.float_info.min
    for elem in data:
        min_x = min(elem[0], min_x)
        max_x = max(elem[0], max_x)

        min_y = min(elem[1], max_x)
        max_y = max(elem[1], max_y)

    min_x -= 2
    min_y -= 2
    max_x += 2
    max_y += 2
    green_squares = set()
    squares = collections.defaultdict(lambda: ".")
    for elem in data:
        squares[elem] = "#"

    for a, b in zip(data, data[1:] + [data[0]]):
        mi_x = min(a[0], b[0])
        ma_x = max(a[0], b[0])
        mi_y = min(a[1], b[1])
        ma_y = max(a[1], b[1])
        x_diff = mi_x - ma_x
        y_diff = mi_y - ma_y
        if x_diff:
            for x in range(mi_x + 1, ma_x):
                squares[(x, a[1])] = "X"

        if y_diff:
            for y in range(mi_y + 1, ma_y):
                squares[(a[0], y)] = "X"

    for y in range(min_y, max_y):
        is_inside = False
        prev = "."
        for x in range(min_x, max_x):
            if squares[(x, y)] in ["X", "#"]:
                is_inside = not is_inside
                continue
            prev = squares[(x, y)]
            squares[(x, y)] = "X"

    largest_area = 0
    for a, b in itertools.combinations(data, 2):
        area = abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
        print(a, b, area)
        allowed_rectangle = True
        # assert squares[a] == "#"
        # assert squares[b] == "#"
        if squares[(a[0], b[1])] == "." or squares[(b[0], a[1])] == ".":
            continue

        if area > largest_area:
            largest_area = area

    for y in range(min_y, max_y):
        for x in range(min_x, max_x + 1):
            print(squares[(x, y)], end="")
        print()
    print(largest_area)


if __name__ == "__main__":
    main()
