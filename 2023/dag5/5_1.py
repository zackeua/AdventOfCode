import sys

seed_to_soil_map = {}
soil_to_fertilizer_map = {}
fertilizer_to_water_map = {}
water_to_light_map = {}
light_to_temperature_map = {}
temperature_to_humidity_map = {}
humidity_to_location_map = {}


def parse_dict(line_number, data):
    d = {}
    line_number += 1
    while line_number < len(data) and data[line_number] != '':
        line = data[line_number]
        dest_start, src_start, range_len = list(map(int, line.split()))
        for i, num in enumerate(range(src_start, src_start + range_len)):
            d[num] = dest_start + i

        line_number += 1
    return d, line_number

def main():
    global seed_to_soil_map
    global soil_to_fertilizer_map
    global fertilizer_to_water_map
    global water_to_light_map
    global light_to_temperature_map
    global temperature_to_humidity_map
    global humidity_to_location_map
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        
        seeds = []
        row = 0
        while row < len(data):
            line = data[row]
            if line == '':
                row += 1
                continue
            if row == 0:
                tmp = line.split(': ')[1]
                seeds.extend(list(map(int, tmp.split())))
            if 'seed-to-soil' in line:
                seed_to_soil_map, row = parse_dict(row, data)
            elif 'soil-to-fertilizer' in line:
                soil_to_fertilizer_map, row = parse_dict(row, data)
            elif 'fertilizer-to-water' in line:
                fertilizer_to_water_map, row = parse_dict(row, data)
            elif 'water-to-light' in line:
                water_to_light_map, row = parse_dict(row, data)
            elif 'light-to-temperature' in line:
                light_to_temperature_map, row = parse_dict(row, data)
            elif 'temperature-to-humidity' in line:
                temperature_to_humidity_map, row = parse_dict(row, data)
            elif 'humidity-to-location' in line:
                humidity_to_location_map, row  = parse_dict(row, data)
            row += 1
        
        print(seeds)
        locations = list(map(seed_to_location, seeds))
        print(locations)
        print(min(locations))


def apply_map(source, mapping):
    if source in mapping:
        return mapping[source]
    else:
        return source

def seed_to_location(seed):
    global seed_to_soil_map
    global soil_to_fertilizer_map
    global fertilizer_to_water_map
    global water_to_light_map
    global light_to_temperature_map
    global temperature_to_humidity_map
    global humidity_to_location_map

    soil  = apply_map(seed, seed_to_soil_map)
    fertilizer = apply_map(soil, soil_to_fertilizer_map)
    water = apply_map(fertilizer, fertilizer_to_water_map)
    light = apply_map(water, water_to_light_map)
    temperature = apply_map(light, light_to_temperature_map)
    humidity = apply_map(temperature, temperature_to_humidity_map)
    location = apply_map(humidity, humidity_to_location_map)
    return location
 

if __name__ == '__main__':
    main()