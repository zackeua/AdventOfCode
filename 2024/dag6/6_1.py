import sys


def next_direction(direction):
    if direction == (-1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (1, 0)
    if direction == (1, 0):
        return (0, -1)
    if direction == (0, -1):
        return (-1, 0)
    assert False, "invaid diretion"


def is_inside(data, current_position):
    return 0 <= current_position[0] <= len(data) - 1 and 0 <= current_position[1] <= len(data[0]) - 1


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [row.strip() for row in data]
        visited = set()
        direction = (-1, 0)

        initial_position = (0, 0)
        for i, line in enumerate(data):
            if '^' in line:
                initial_position = (i, line.find('^'))

        data = [[elem for elem in row] for row in data]
        current_position = initial_position

        while is_inside(data, current_position):
            visited.add(current_position)
            # data[current_position[0]][current_position[1]] = 'X'

            potential_position = (
                current_position[0] + direction[0], current_position[1] + direction[1])
            if is_inside(data, potential_position):
                if data[potential_position[0]][potential_position[1]] != '#':
                    current_position = potential_position
                else:
                    direction = next_direction(direction)
            else:
                current_position = potential_position
            # for row in data:
            # print(''.join(row))
            # input()
        print(len(visited))


if __name__ == '__main__':
    main()
