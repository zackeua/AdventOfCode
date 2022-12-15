import sys

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open(sys.argv[1], 'r') as f:
    with open(sys.argv[2], 'w') as out_f:
        data = f.readlines()
        out_f.write(f'number_of_sensors = {len(data)};\n')
        x_position_of_sensor = []
        y_position_of_sensor = []
        distance_for_sensor = []
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
            x_position_of_sensor.append(separate_values[3])
            y_position_of_sensor.append(separate_values[5])
            distance = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))
            distance_for_sensor.append(str(distance))

        out_f.write(f'x_position_of_sensor = [{",".join(x_position_of_sensor)}];\n')
        out_f.write(f'y_position_of_sensor = [{",".join(y_position_of_sensor)}];\n')
        out_f.write(f'distance_for_sensor = [{",".join(distance_for_sensor)}];\n')

        

