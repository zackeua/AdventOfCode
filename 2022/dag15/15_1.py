import sys

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        sensor_list = []
        beacon_list = []
        magic_row = 2000000
        covered = set()
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
            if sensor_y <= magic_row and  magic_row <= sensor_y + distance:
                i = 0
                while magic_row <= sensor_y + distance - i:
                    if (sensor_x + i, magic_row) not in beacon_list:
                        covered.add((sensor_x + i, magic_row))
                    if (sensor_x - i, magic_row) not in beacon_list:
                        covered.add((sensor_x - i, magic_row))
                    i += 1
            elif sensor_y - distance <= magic_row and magic_row <= sensor_y:
                i = 0
                while sensor_y - distance + i <= magic_row:
                    if (sensor_x + i, magic_row) not in beacon_list:
                        covered.add((sensor_x + i, magic_row))
                    if (sensor_x - i, magic_row) not in beacon_list:
                        covered.add((sensor_x - i, magic_row))
                    i += 1
        print(len(covered))
if __name__ == '__main__':
    main()
