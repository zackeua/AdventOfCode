import sys


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_possible_coordinates(sensor_list, sensor_distance):
    for sensor in sensor_list:
        distance = sensor_distance[sensor]
        p1 = (sensor[0] + distance + 1, sensor[1])
        p2 = (sensor[0], sensor[1] + distance + 1)
        p3 = (sensor[0] - distance - 1, sensor[1])
        p4 = (sensor[0], sensor[1] - distance - 1)
        current_pos = p1
        while current_pos != p2:
            yield current_pos
            current_pos = (current_pos[0] - 1, current_pos[1] + 1)
        while current_pos != p3:
            yield current_pos
            current_pos = (current_pos[0] - 1, current_pos[1] - 1)
        while current_pos != p4:
            yield current_pos
            current_pos = (current_pos[0] + 1, current_pos[1] - 1)
        while current_pos != p1:
            yield current_pos
            current_pos = (current_pos[0] + 1, current_pos[1] + 1)


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        sensor_list = []
        beacon_list = []
        sensor_distance = {}
        for row in data:
            row = row.replace(',', '')
            row = row.replace(',', '')
            row = row.replace(':', '')
            row = row.replace('=', ' ')
            separate_values = row.split(' ')

            sensor_x = int(separate_values[3])
            sensor_y = int(separate_values[5])
            beacon_x = int(separate_values[11])
            beacon_y = int(separate_values[13])
            sensor_list.append((sensor_x, sensor_y))
            beacon_list.append((beacon_x, beacon_y))
            distance = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))
            sensor_distance[(sensor_x, sensor_y)] = distance

        for coordinate in get_possible_coordinates(sensor_list, sensor_distance):
            x_coord, y_coord = coordinate
            if not (0 <= x_coord <= 4000000):
                continue
            if not (0 <= y_coord <= 4000000):
                continue
            if (x_coord, y_coord) not in beacon_list:
                in_range = False
                for sensor in sensor_list:
                    sensor_x, sensor_y = sensor
                    distance = sensor_distance[sensor]
                    if sensor_y <= y_coord <= sensor_y + distance and sensor_x - distance <= x_coord <= sensor_x + distance:
                        i = 0
                        while y_coord <= sensor_y + distance - i:
                            if x_coord - i <= sensor_x <= x_coord + i:
                                in_range = True
                                break
                            i += 1
                    elif sensor_y - distance <= y_coord <= sensor_y and sensor_x - distance <= x_coord <= sensor_x + distance:
                        i = 0
                        while sensor_y - distance + i <= y_coord:
                            if x_coord - i <= sensor_x <= x_coord + i:
                                in_range = True
                                break
                            i += 1
                    if in_range:
                        print('break')

                        break
                if not in_range:
                    print(x_coord, y_coord)
                    print(x_coord * 4000000 + y_coord)
                    sys.exit()
            print(f'{x_coord=}, {y_coord=}')
if __name__ == '__main__':
    main()
