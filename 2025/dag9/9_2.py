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

    # for a, b in zip(data, data[1:] + [data[0]]):
    #     mi_x = min(a[0], b[0])
    #     ma_x = max(a[0], b[0])
    #     mi_y = min(a[1], b[1])
    #     ma_y = max(a[1], b[1])
    #     x_diff = mi_x - ma_x
    #     y_diff = mi_y - ma_y
    #     if x_diff != 0:
    #         for x in range(mi_x + 1, ma_x):
    #             squares[(x, a[1])] = "X"
    #
    #     if y_diff != 0:
    #         for y in range(mi_y + 1, ma_y):
    #             squares[(a[0], y)] = "X"

    largest_area = 0
    for a, b in itertools.combinations(data, 2):
        valid_rectangle = True
        for elem1, elem2 in zip(data, data[1:] + [data[0]]):
            # (a[0], a[1])              (a[0], b[1])
            #
            #                 X (elem1)
            #                 |
            # (b[0], a[1])    |         (b[0], b[1])
            #                 |
            #                 |
            #                 |
            #                 X (elem2)

            line_min_x = min(elem1[0], elem2[0])
            line_max_x = max(elem1[0], elem2[0])
            line_min_y = min(elem1[1], elem2[1])
            line_max_y = max(elem1[1], elem2[1])

            # line 1: (a[0], a[1]) -> (a[0], b[1])
            y_min = min(a[1], b[1])
            y_max = max(a[1], b[1])
            x = a[0]

            if (
                line_min_x < x < line_max_x
                and y_min < line_min_y < y_max
                and y_min < line_max_y < y_max
            ):
                valid_rectangle = False
                break
            # line 2: (a[0], a[1]) -> (b[0], a[1])
            x_min = min(a[0], b[0])
            x_max = max(a[0], b[0])
            y = a[1]

            if (
                line_min_y < y < line_max_y
                and x_min < line_min_x < x_max
                and x_min < line_max_x < x_max
            ):
                valid_rectangle = False
                break
            # line 3: (b[0], a[1]) -> (b[0], b[1])
            y_min = min(a[1], b[1])
            y_max = max(a[1], b[1])
            x = b[0]
            if (
                line_min_x < x < line_max_x
                and y_min < line_min_y < y_max
                and y_min < line_max_y < y_max
            ):
                valid_rectangle = False
                break

            # line 4: (a[0], b[1]) -> (b[0], b[1])
            x_min = min(a[0], b[0])
            x_max = max(a[0], b[0])
            y = b[1]
            if (
                line_min_y < y < line_max_y
                and x_min < line_min_x < x_max
                and x_min < line_max_x < x_max
            ):
                valid_rectangle = False
                break

        if not valid_rectangle:
            continue
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if area > largest_area:
            print(a, b, area)
            largest_area = area

    # plt.plot(
    #     [a for a, b in squares.keys() if squares[(a, b)] in "#X"],
    #     [b for a, b in squares.keys() if squares[(a, b)] in "#X"],
    #     ".",
    # )
    # plt.show()
    #
    # for y in range(min_y, max_y):
    #     for x in range(min_x, max_x + 1):
    #         print(squares[(x, y)], end="")
    #     print()
    print(largest_area)
    # print(max_x - min_x)
    # print(max_y - min_y)


if __name__ == "__main__":
    main()
