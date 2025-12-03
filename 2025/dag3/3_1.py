import sys


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[int(c) for c in line] for line in data]
        # print(data)

    total = 0
    for battery in data:
        max_cell = max(battery)
        max_cell_index = battery.index(max_cell)
        if max_cell_index == len(battery) - 1:
            max_cell = max(battery[:-1])
        max_cell_index = battery.index(max_cell)
        second_max_cell = max(battery[max_cell_index + 1 :])
        battery_total = int(f"{max_cell}{second_max_cell}")
        total += battery_total
    print(total)


if __name__ == "__main__":
    main()
