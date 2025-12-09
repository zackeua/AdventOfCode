# /// script
# dependencies = [
#   "tqdm",
#   "matplotlib",
# ]
# ///

import sys
import itertools
import collections
import tqdm
import matplotlib.pyplot as plt


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
        if x_diff != 0:
            for x in range(mi_x + 1, ma_x):
                squares[(x, a[1])] = "X"

        if y_diff != 0:
            for y in range(mi_y + 1, ma_y):
                squares[(a[0], y)] = "X"

    to_color = [((min_x + max_x) // 2, (min_y + max_y) // 4)]
    # to_color = [(data[0][0] + 1, data[0][1] + 1)]

    i = 0
    while tqdm.tqdm(to_color):
        i += 1
        if i % 10000 == 0:
            plt.plot(
                [a for a, b in squares.keys() if squares[(a, b)] in "#X"],
                [b for a, b in squares.keys() if squares[(a, b)] in "#X"],
                ".",
            )
            plt.show()

        # print(to_color)
        a, b = to_color.pop()
        if (a + 1, b) not in squares and (a + 1, b) not in to_color:
            to_color.append((a + 1, b))

        if (a - 1, b) not in squares and (a - 1, b) not in to_color:
            to_color.append((a - 1, b))

        if (a, b + 1) not in squares and (a, b + 1) not in to_color:
            to_color.append((a, b + 1))

        if (a, b - 1) not in squares and (a, b - 1) not in to_color:
            to_color.append((a, b - 1))
        # print(to_color)
        # input()
        squares[(a, b)] = "X"

    largest_area = 0
    for a, b in itertools.combinations(data, 2):
        # print(a, b, area)
        allowed_rectangle = True
        # assert squares[a] == "#"
        # assert squares[b] == "#"
        if squares[(a[0], b[1])] == "." or squares[(b[0], a[1])] == ".":
            continue

        for y in range(a[1], b[1]):
            if squares[(a[0], y)] == "." or squares[(b[0], y)] == ".":
                allowed_rectangle = False
                break
        if not allowed_rectangle:
            continue

        for y in range(a[0], b[0]):
            if squares[(x, a[1])] == "." or squares[(x, b[1])] == ".":
                allowed_rectangle = False
                break
        if not allowed_rectangle:
            continue

        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if area > largest_area:
            largest_area = area

    # plt.plot(
    # [a for a, b in squares.keys() if squares[(a, b)] in "#X"],
    # [b for a, b in squares.keys() if squares[(a, b)] in "#X"],
    # ".",
    # )
    # plt.show()

    # for y in range(min_y, max_y):
    # for x in range(min_x, max_x + 1):
    # print(squares[(x, y)], end="")
    # print()
    print(largest_area)
    # print(max_x - min_x)
    # print(max_y - min_y)


if __name__ == "__main__":
    main()
