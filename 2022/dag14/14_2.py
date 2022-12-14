import sys

def get_iterable(start_point, end_point):
    if start_point[0] != end_point[0]:
        start = min([start_point[0], end_point[0]])
        stop = max([start_point[0], end_point[0]]) + 1
        for i in range(start, stop):
            yield i, end_point[1]
    else:
        start = min([start_point[1], end_point[1]])
        stop = max([start_point[1], end_point[1]]) + 1        
        for i in range(start, stop):
            yield start_point[0], i


def show_cave(rock_positions, sand_positions, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if (x, y) in rock_positions:
                print('#', end='')
            elif (x, y) in sand_positions:
                print('o', end='')
            else:
                print('.', end='')
        print()

def next_sand(current_position, rock_positions, sand_positions):
    if (current_position[0], current_position[1] + 1) not in rock_positions and (current_position[0], current_position[1] + 1) not in sand_positions:
        return (current_position[0], current_position[1] + 1)
    elif (current_position[0] - 1, current_position[1] + 1) not in rock_positions and (current_position[0] - 1, current_position[1] + 1) not in sand_positions:
        return (current_position[0] - 1, current_position[1] + 1)
    elif (current_position[0] + 1, current_position[1] + 1) not in rock_positions and (current_position[0] + 1, current_position[1] + 1) not in sand_positions:
        return (current_position[0] + 1, current_position[1] + 1)
    else:
        return None

def step(rock_positions, sand_positions, sand_inlet, min_x, max_x, min_y, max_y):
    current_sand_position = sand_inlet
    next_sand_position = next_sand(current_sand_position, rock_positions, sand_positions)
    if next_sand_position is None:
        return sand_positions, False
    while next_sand_position is not None:
        if next_sand_position[1] > max_y + 1:
            sand_positions.add(current_sand_position)
            return sand_positions, True
        current_sand_position = next_sand_position
        next_sand_position = next_sand(
            current_sand_position, rock_positions, sand_positions)
    sand_positions.add(current_sand_position)
    return sand_positions, True


def main():

    with open(sys.argv[1], 'r') as f:
        data = [row.replace('\n', '') for row in f.readlines()]
        data = [row.split(' -> ') for row in data]
        rock_positions = set()
        sand_positions = set()
        sand_inlet = (500, 0)
        min_x_rock_position = sand_inlet[0]
        max_x_rock_position = sand_inlet[0]
        min_y_rock_position = sand_inlet[1]
        max_y_rock_position = sand_inlet[1]
        for row in data:
            for i, elem in enumerate(row[1:]):
                start_point = tuple(map(int, row[i].split(',')))
                end_point = tuple(map(int, elem.split(',')))
                iterable = list(get_iterable(start_point, end_point))
                x = [i[0] for i in iterable]
                y = [i[1] for i in iterable]
                min_x = min(x)
                max_x = max(x)
                min_y = min(y)
                max_y = max(y)
                if min_x_rock_position > min_x:
                    min_x_rock_position = min_x
                if max_x_rock_position < max_x:
                    max_x_rock_position = max_x
                if min_y_rock_position > min_y:
                    min_y_rock_position = min_y
                if max_y_rock_position < max_y:
                    max_y_rock_position = max_y
                rock_positions = rock_positions.union(set(iterable))
        #print(min_x_rock_position, max_x_rock_position + 1, min_y_rock_position, max_y_rock_position + 1)
        show_cave(rock_positions, sand_positions, min_x_rock_position, max_x_rock_position + 1, min_y_rock_position, max_y_rock_position + 1)
        continue_stepping = True
        while continue_stepping:
            sand_positions, continue_stepping = step(rock_positions, sand_positions, sand_inlet, min_x_rock_position, max_x_rock_position, min_y_rock_position, max_y_rock_position)
            #show_cave(rock_positions, sand_positions, min_x_rock_position, max_x_rock_position + 1, min_y_rock_position, max_y_rock_position + 1)
        print(len(sand_positions) + 1)
if __name__ == '__main__':
    main()
