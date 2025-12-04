import sys


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = ["." + line.strip() + "." for line in data]
        data = ["." * len(data[0])] + data + ["." * len(data[0])]
        data = [[c for c in line] for line in data]

    prev_total = -1
    total = 0
    while prev_total != total:
        prev_total = total
        for row in range(1, len(data) - 1):
            for col in range(1, len(data[0]) - 1):
                adjacent = 0
                if data[row][col] in [".", "x"]:
                    continue
                dirs = (
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                )
                for row_i, col_i in dirs:
                    adjacent += data[row + row_i][col + col_i] == "@"
                if adjacent < 4:
                    total += 1
                    data[row][col] = "x"
            # print("".join(data[row]))
        # print(total - prev_total)
        # print(total, prev_total)
        # print("\n" * 3)
        # input()
    print(total)


if __name__ == "__main__":
    main()
