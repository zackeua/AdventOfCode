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


def search(input_data, initial_position):

    visited_points = set()
    direction = (-1, 0)
    current_position = initial_position
    data = [[elem for elem in row] for row in input_data]
    while is_inside(data, current_position):

        visited_points.add(current_position)
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

    positions_to_consider = set()
    for p in visited_points:
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                considering = (p[0] + i, p[1] + j)
                if is_inside(data, considering):
                    positions_to_consider.add(considering)

    loop_count = 0
    for (i, j) in positions_to_consider:
        if (i, j) == initial_position:
            continue

        visited = set()
        direction = (-1, 0)
        current_position = initial_position
        run_loop = True
        data = [[elem for elem in row] for row in input_data]
        data[i][j] = '#'
        while is_inside(data, current_position) and run_loop:
            if (current_position, direction) in visited:  # in loop
                loop_count += 1
                run_loop = False

            visited.add((current_position, direction))
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
            #    print(''.join(row))
            # input()

    return loop_count


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [row.strip() for row in data]

        initial_position = (0, 0)
        for i, line in enumerate(data):
            if '^' in line:
                initial_position = (i, line.find('^'))

        result = search(data, initial_position)
        print(result)


if __name__ == '__main__':
    main()
