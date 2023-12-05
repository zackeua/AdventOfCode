import sys


soil_to_seed_map = []
fertilizer_to_soil_map = []
water_to_fertilizer_map = []
light_to_water_map = []
temperature_to_light_map = []
humidity_to_temperature_map = []
location_to_humidity_map = []


def parse_mapping(line_number, data):
    d = []
    line_number += 1
    while line_number < len(data) and data[line_number] != '':
        line = data[line_number]
        dest_start, src_start, range_len = tuple(map(int, line.split()))
        d.append((dest_start, src_start, range_len))
        line_number += 1
    return d, line_number

def parse_seeds(line):
    seeds = []
    seed_list = list(map(int, line.split()))
    for i, elem in enumerate(seed_list[::2]):
        seeds.append((elem, seed_list[i*2 + 1]))
    return seeds

def main():
    global soil_to_seed_map
    global fertilizer_to_soil_map
    global water_to_fertilizer_map
    global light_to_water_map
    global temperature_to_light_map
    global humidity_to_temperature_map
    global location_to_humidity_map
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
                seed_ranges = parse_seeds(tmp)
            if 'seed-to-soil' in line:
                soil_to_seed_map, row = parse_mapping(row, data)
            elif 'soil-to-fertilizer' in line:
                fertilizer_to_soil_map, row = parse_mapping(row, data)
            elif 'fertilizer-to-water' in line:
                water_to_fertilizer_map, row = parse_mapping(row, data)
            elif 'water-to-light' in line:
                light_to_water_map, row = parse_mapping(row, data)
            elif 'light-to-temperature' in line:
                temperature_to_light_map, row = parse_mapping(row, data)
            elif 'temperature-to-humidity' in line:
                humidity_to_temperature_map, row = parse_mapping(row, data)
            elif 'humidity-to-location' in line:
                location_to_humidity_map, row  = parse_mapping(row, data)
            row += 1
        
        # reverse search
        location = 0
        while True:

            seed = location_to_seed(location)

            for seed_range in seed_ranges:
                #print(location)
                if seed_range[0] <= seed < seed_range[0] + seed_range[1]:
                    print(location)
                    sys.exit()

            location += 1



def apply_map(source, mapping):
    for mapping_range in mapping:
        if mapping_range[0] <= source < mapping_range[0] + mapping_range[2]:
            return  mapping_range[1] + source - mapping_range[0]
    return source

def location_to_seed(location):
    global soil_to_seed_map
    global fertilizer_to_soil_map
    global water_to_fertilizer_map
    global light_to_water_map
    global temperature_to_light_map
    global humidity_to_temperature_map
    global location_to_humidity_map

    humidity = apply_map(location, location_to_humidity_map)
    temperature = apply_map(humidity, humidity_to_temperature_map)
    light = apply_map(temperature, temperature_to_light_map)
    water = apply_map(light, light_to_water_map)
    fertilizer = apply_map(water, water_to_fertilizer_map)
    soil = apply_map(fertilizer, fertilizer_to_soil_map)
    seed  = apply_map(soil, soil_to_seed_map)
    return seed
 

if __name__ == '__main__':
    main()