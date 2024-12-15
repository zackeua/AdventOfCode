import sys


UP = complex(-1, 0)
DOWN = complex(1, 0)
LEFT = complex(0, -1)
RIGHT = complex(0, 1)

WALL = '#'
BOX = 'O'


def parse_warehouse_map(warehouse_map):
    robot_position = complex(0, 0)
    warehouse_map_dict = {}
    for i, line in enumerate(warehouse_map):
        for j, elem in enumerate(line):
            if elem == '#':
                warehouse_map_dict[complex(i, j)] = WALL
            elif elem == 'O':
                warehouse_map_dict[complex(i, j)] = BOX
            elif elem == '@':
                robot_position = complex(i, j)
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


def move_boxes(warehouse_map, robot_position, direction):
    test_position = robot_position
    while True:

        test_position = test_position + direction
        test_elem = warehouse_map.get(test_position, None)

        if test_elem is None:
            warehouse_map[test_position] = BOX
            robot_position = robot_position + direction
            warehouse_map[robot_position] = None
            return warehouse_map, robot_position
        elif test_elem == WALL:
            return warehouse_map, robot_position


def move_robot(warehouse_map, robot_position, robot_moves):
    for move in robot_moves:
        direction = move_to_direction(move)

        test_robot_position = robot_position + direction

        at_location = warehouse_map.get(test_robot_position, None)
        if at_location is None:
            robot_position = test_robot_position
        elif at_location == WALL:
            continue
        elif at_location == BOX:
            warehouse_map, robot_position = move_boxes(
                warehouse_map, robot_position, direction)

    return warehouse_map


def calculate_gps_coordinate(warehouse_map: dict):
    total = 0
    for key in warehouse_map.keys():
        if warehouse_map[key] == BOX:
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

    warehouse_dictionary = move_robot(
        warehouse_dictionary, robot_position, robot_moves)

    result = calculate_gps_coordinate(warehouse_dictionary)
    print(result)


if __name__ == '__main__':
    main()
