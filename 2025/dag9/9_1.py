import sys
import itertools


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [list(map(int, line.split(","))) for line in data]
        # print(data)
    largest_area = 0
    for a, b in itertools.combinations(data, 2):
        area = abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
        if area > largest_area:
            largest_area = area
        # print(a, b, area)
    print(largest_area)


if __name__ == "__main__":
    main()
