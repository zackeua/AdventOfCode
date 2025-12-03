import sys
import itertools


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[int(c) for c in line] for line in data]
        # print(data)

    total = 0
    for battery in data:
        local_total = 0
        max_cell_index = -1
        for i in range(12):
            lower_bound = max(max_cell_index + 1, i)
            upper_bound = -12 + i + 1

            try:
                max_cell = max(battery[lower_bound:upper_bound])
            except:
                max_cell = max(battery[lower_bound:])

            max_cell_index = battery[lower_bound:].index(max_cell) + lower_bound
            local_total *= 10
            local_total += int(max_cell)

        total += local_total
    print(total)


if __name__ == "__main__":
    main()
