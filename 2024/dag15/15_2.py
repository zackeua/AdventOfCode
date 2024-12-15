import sys


UP = complex(-1, 0)
DOWN = complex(1, 0)
LEFT = complex(0, -1)
RIGHT = complex(0, 1)

WALL = '#'
BOX = 'O'
LEFT_BOX = '['
RIGHT_BOX = ']'


def show_warehouse_map(warehouse_map, robot_position, x_max, y_max):
    for i in range(0, x_max):
        for j in range(0, y_max):
            if complex(i, j) == robot_position:
                print('@', end='')
            else:
                elem = warehouse_map.get(complex(i, j), None)
                if elem is None:
                    print('.', end='')
                else:
                    print(elem, end='')
        print()


def parse_warehouse_map(warehouse_map):
    robot_position = complex(0, 0)
    warehouse_map_dict = {}
    for i, line in enumerate(warehouse_map):
        for j, elem in enumerate(line):
            if elem == WALL:
                warehouse_map_dict[complex(i, j * 2)] = WALL
                warehouse_map_dict[complex(i, j * 2 + 1)] = WALL
            elif elem == BOX:
                warehouse_map_dict[complex(i, j * 2)] = LEFT_BOX
                warehouse_map_dict[complex(i, j * 2 + 1)] = RIGHT_BOX
            elif elem == '@':
                robot_position = complex(i, j * 2)
    return warehouse_map_dict, robot_position


def move_to_direction(move):
    if move == '^':
        return UP
    if move == '<':
        return LEFT
    if move == '>':
        return RIGHT
    if move == 'v':
        return DOWN


def move_boxes(warehouse_map, robot_position, move):

    direction = move_to_direction(move)
    if direction == RIGHT or direction == LEFT:
        test_position = robot_position
        while True:
            test_position = test_position + direction
            test_elem = warehouse_map.get(test_position, None)
            if test_elem is None:
                while test_position != robot_position + direction:
                    warehouse_map[test_position] = warehouse_map[test_position - direction]
                    warehouse_map[test_position - direction] = None
                    test_position = test_position - direction
                robot_position = robot_position + direction
                return warehouse_map, robot_position
            elif test_elem == WALL:
                return warehouse_map, robot_position
    if direction == UP or direction == DOWN:
        test_position = robot_position + direction
        positions_to_test = []
        positions_to_test.append(test_position)
        loop = True
        while loop:
            loop = False
            for elem in positions_to_test:
                test_position = elem
                test_element = warehouse_map.get(test_position, None)
                if test_element == WALL:
                    return warehouse_map, robot_position
                elif test_element == LEFT_BOX:
                    if test_position + direction not in positions_to_test:
                        positions_to_test.append(test_position + direction)
                        loop = True
                    if test_position + RIGHT not in positions_to_test:
                        positions_to_test.append(test_position + RIGHT)
                        loop = True
                elif test_element == RIGHT_BOX:
                    # print(test_position + direction)
                    # print(test_position + LEFT)
                    if test_position + direction not in positions_to_test:
                        positions_to_test.append(test_position + direction)
                        loop = True
                    if test_position + LEFT not in positions_to_test:
                        positions_to_test.append(test_position + LEFT)
                        loop = True

        # print(positions_to_test)
        while positions_to_test:
            position = positions_to_test.pop()
            elem = warehouse_map.get(position + direction, None)

            if elem is None:
                warehouse_map[position +
                              direction] = warehouse_map.get(position, None)
                warehouse_map[position] = None

        return warehouse_map, robot_position + direction


def move_robot(warehouse_map, robot_position, robot_moves):
    for move in robot_moves:

        direction = move_to_direction(move)
        test_robot_position = robot_position + direction

        at_location = warehouse_map.get(test_robot_position, None)
        if at_location is None:
            robot_position = test_robot_position
        elif at_location == WALL:
            continue
        elif at_location == LEFT_BOX or at_location == RIGHT_BOX:
            warehouse_map, robot_position = move_boxes(
                warehouse_map, robot_position, move)
        # show_warehouse_map(warehouse_map, robot_position, 10, 20)
        # input()

    return warehouse_map


def calculate_gps_coordinate(warehouse_map: dict):
    total = 0
    for key in warehouse_map.keys():
        if warehouse_map[key] == LEFT_BOX:
            total += int(100 * key.real + key.imag)

    return total


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    warehouse_map = []
    robot_moves = ''
    add_warehouse_line = True
    for line in data:
        if line == '':
            add_warehouse_line = False
        elif add_warehouse_line:
            warehouse_map.append(line)
        else:
            robot_moves += line

    warehouse_dictionary, robot_position = parse_warehouse_map(warehouse_map)

    # show_warehouse_map(warehouse_dictionary, robot_position, 11, 20)

    warehouse_dictionary = move_robot(
        warehouse_dictionary, robot_position, robot_moves)

    result = calculate_gps_coordinate(warehouse_dictionary)
    print(result)


if __name__ == '__main__':
    main()
