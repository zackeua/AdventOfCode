import sys


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


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
        for y_coord in range(0, 4000001): #range(0, 21): #
            for x_coord in range(0, 4000001): #range(0, 21): #
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
                print(f'{x_coord=}')
            print(f'{y_coord=}')
if __name__ == '__main__':
    main()
