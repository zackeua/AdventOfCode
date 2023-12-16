import sys


def rotate_90_counterclockwise(grid: list[list[str]]):
    data = [line.copy() for line in grid]
    for i, line in enumerate(grid):
        for j, elem in enumerate(line):
            data[j][len(line)-i-1] = elem
    return data


def tilt_north(grid: list[list[str]]):
    data = [line.copy() for line in grid]
    for _ in range(len(data)):
        for i, line in enumerate(data[1:], start=1):
            for j, elem in enumerate(line):
                if data[i-1][j] == '.' and elem == 'O':
                    data[i-1][j] = 'O'
                    data[i][j] = '.'
    return data


def cycle(grid: list[list[str]]):
    data = tilt_north(grid)
    data = rotate_90_counterclockwise(data)
    data = tilt_north(data)
    data = rotate_90_counterclockwise(data)
    data = tilt_north(data)
    data = rotate_90_counterclockwise(data)
    data = tilt_north(data)
    data = rotate_90_counterclockwise(data)
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
        visited = []
        first_cycle = None
        second_cycle = None
        for i in range(1, 10000):
            visited.append(data)
            data = cycle(data)
            # print(f'After {i} cycles:')
            # for line in data:
            #     print(''.join(line))
            # print()
            if data in visited:
                if first_cycle is None:
                    first_cycle = i
                elif data == visited[first_cycle]:
                    if second_cycle is None:
                        second_cycle = i
                        break
        # print(f'First cycle: {first_cycle}')
        # print(f'Second cycle: {second_cycle}')

        cycle_length = second_cycle - first_cycle

        index = (1000000000 - first_cycle) % cycle_length + first_cycle

        print(get_score(visited[index]))

if __name__ == '__main__':
    main()
