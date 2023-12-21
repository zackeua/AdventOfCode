import sys


def find_stones(data):

    stones = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                stones.add((i, j))
    return stones


def get_starting_point(data):

    position = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                position.add((i, j))
                return position


def step(data, stones, positions):

    new_positions = set()
    for position in positions:
        if (position[0], position[1]+1) not in stones:
            new_positions.add((position[0], position[1]+1))
        if (position[0]+1, position[1]) not in stones:
            new_positions.add((position[0]+1, position[1]))
        if (position[0], position[1]-1) not in stones:
            new_positions.add((position[0], position[1]-1))
        if (position[0]-1, position[1]) not in stones:
            new_positions.add((position[0]-1, position[1]))
    return new_positions


def show(data, positions):

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if (i, j) in positions:
                print('O', end='')
            else:
                print(char, end='')
        print()


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = ['#' + line.strip() + '#' for line in data]
        data = ['#'*len(data[0])] + data + ['#'*len(data[0])]
        stones = find_stones(data)
        points = get_starting_point(data)
        steps = 64
        for i in range(steps):
            points = step(data, stones, points)

        print(len(points))


if __name__ == '__main__':
    main()
