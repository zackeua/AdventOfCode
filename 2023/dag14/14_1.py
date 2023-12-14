import sys


def tilt_north(grid: list[list[str]]):
    data = [line.copy() for line in grid]
    for _ in range(len(data)):
        for i, line in enumerate(data[1:], start=1):
            for j, elem in enumerate(line):
                if data[i-1][j] == '.' and elem == 'O':
                    data[i-1][j] = 'O'
                    data[i][j] = '.'
    return data


def get_score(grid: list[list[str]]):
    total = 0
    for i, line in enumerate(grid[::-1], start=1):
        total += i * line.count('O')
    return total


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[c for c in line.strip()] for line in data]
        # for line in data:
        #     print(''.join(line))
        # print()
        # print()
        tilted_data = tilt_north(data)
        # for line in tilted_data:
        #     print(''.join(line))
        result = get_score(tilted_data)
        print(result)


if __name__ == '__main__':
    main()
