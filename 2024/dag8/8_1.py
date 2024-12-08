import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    antennas = {}

    for i, line in enumerate(data):
        for j, elem in enumerate(line):
            if elem != '.':
                if elem not in antennas:
                    antennas[elem] = []
                antennas[elem].append((i, j))

    antinode_locations = set()

    x_min = -1
    x_max = len(data)
    y_min = -1
    y_max = len(data[0])

    for key in antennas.keys():
        for a1 in antennas[key]:
            for a2 in antennas[key]:
                if a1 == a2:
                    continue

                diff_vector = (a1[0] - a2[0], a1[1] - a2[1])

                p1 = (a1[0] - diff_vector[0], a1[1] - diff_vector[1])
                p2 = (a1[0] + diff_vector[0], a1[1] + diff_vector[1])
                p3 = (a2[0] - diff_vector[0], a2[1] - diff_vector[1])
                p4 = (a2[0] + diff_vector[0], a2[1] + diff_vector[1])

                if p1 == a2:
                    if x_min < p2[0] < x_max and y_min < p2[1] < y_max:
                        antinode_locations.add(p2)
                    if x_min < p3[0] < x_max and y_min < p3[1] < y_max:
                        antinode_locations.add(p3)
                elif p2 == a2:
                    if x_min < p1[0] < x_max and y_min < p1[1] < y_max:
                        antinode_locations.add(p1)
                    if x_min < p4[0] < x_max and y_min < p4[1] < y_max:
                        antinode_locations.add(p4)
                else:
                    assert False

    print(len(antinode_locations))


if __name__ == '__main__':
    main()
