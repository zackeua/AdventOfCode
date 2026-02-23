# /// script
# dependencies = [
#   "tqdm",
#   "matplotlib",
# ]
# ///

import sys
import itertools
import collections
# import tqdm
# import matplotlib.pyplot as plt


def lines_intersect(line_1, line_2):
    line_1_min_x = min(line_1[0][0], line_1[1][0])
    line_1_max_x = max(line_1[0][0], line_1[1][0])
    line_1_min_y = min(line_1[0][1], line_1[1][1])
    line_1_max_y = max(line_1[0][1], line_1[1][1])

    line_2_min_x = min(line_2[0][0], line_2[1][0])
    line_2_max_x = max(line_2[0][0], line_2[1][0])
    line_2_min_y = min(line_2[0][1], line_2[1][1])
    line_2_max_y = max(line_2[0][1], line_2[1][1])

    if line_1_min_x == line_1_max_x:
        if line_2_min_x == line_2_max_x:
            # line_1a - line_2a - line_1b - line_2a OR
            # line_2a - line_1a - line_2b - line_1b
            line_1_outside_line_2 = line_1_min_y < line_2_min_y < line_1_max_y
            line_2_outside_line_1 = line_2_min_y < line_1_min_y < line_2_max_y
            return line_1_outside_line_2 or line_2_outside_line_1
        elif line_2_min_y == line_2_max_y:
            # lines crossing each other
            line_2_inside_line_1_domain = line_1_min_y < line_2_min_y < line_1_max_y
            line_1_inside_line_2_domain = line_2_min_x < line_1_min_x < line_2_max_x
            return line_2_inside_line_1_domain and line_1_inside_line_2_domain
        else:
            assert False
    elif line_1_min_y == line_1_max_y:
        if line_2_min_x == line_2_max_x:
            # lines crossing each other
            line_2_inside_line_1_domain = line_1_min_y < line_2_min_y < line_1_max_y
            line_1_inside_line_2_domain = line_2_min_x < line_1_min_x < line_2_max_x
            return line_2_inside_line_1_domain and line_1_inside_line_2_domain
        elif line_2_min_y == line_2_max_y:
            # line_1a - line_2a - line_1b - line_2a OR
            # line_2a - line_1a - line_2b - line_1b
            line_1_outside_line_2 = line_1_min_x < line_2_min_x < line_1_max_x
            line_2_outside_line_1 = line_2_min_x < line_1_min_x < line_2_max_x
            return line_1_outside_line_2 or line_2_outside_line_1
        else:
            assert False
    else:
        assert False


def line_intersects_polygon(line, polygon):
    for temporary_line in polygon:
        if lines_intersect(line, temporary_line):
            return True
    return False


def rectangle_intersects_polygon(rectangle, polygon):
    a, b = rectangle
    point_1 = a
    point_2 = (a[0], b[1])
    point_3 = (b[0], a[1])
    point_4 = b

    if line_intersects_polygon((point_1, point_2), polygon):
        return True
    if line_intersects_polygon((point_1, point_3), polygon):
        return True
    if line_intersects_polygon((point_2, point_4), polygon):
        return True
    if line_intersects_polygon((point_3, point_4), polygon):
        return True
    return False


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [tuple(map(int, line.split(","))) for line in data]
        # print(data)

    edge_pairs = list(zip(data, data[1:] + [data[0]]))

    largest_area = 0
    area_pairs = itertools.combinations(data, 2)
    for rectangle in area_pairs:
        valid_rectangle = not rectangle_intersects_polygon(rectangle, edge_pairs)

        if not valid_rectangle:
            continue
        a, b = rectangle
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        # area = (abs(a[0] - b[0])) * (abs(a[1] - b[1]))

        print(a, b, area)
        if area > largest_area:
            # print(a, b, area)
            largest_area = area

    print(largest_area)


if __name__ == "__main__":
    main()
