import sys


def calculate_area_and_boundary(garden):
    visited_slots = set()
    total = 0
    for i in range(1, len(garden) - 1):
        for j in range(1, len(garden[0]) - 1):
            if garden[i][j] == '.':
                assert False, f'index: {i}, {j}'

            if (i, j) in visited_slots:
                continue

            visited_slots.add(((i, j)))

            region = [(i, j)]
            area = 0
            boundary = 0

            while region:
                (x, y) = region[0]
                region = region[1:]

                elem = garden[x][y]
                area += 1

                visited_slots.add(((x, y)))

                if garden[x - 1][y] != elem:
                    boundary += 1
                elif (x - 1, y) not in visited_slots and (x - 1, y) not in region:
                    region.append((x - 1, y))

                if garden[x + 1][y] != elem:
                    boundary += 1
                elif (x + 1, y) not in visited_slots and (x + 1, y) not in region:
                    region.append((x + 1, y))

                if garden[x][y - 1] != elem:
                    boundary += 1
                elif (x, y - 1) not in visited_slots and (x, y - 1) not in region:
                    region.append((x, y - 1))

                if garden[x][y + 1] != elem:
                    boundary += 1
                elif (x, y + 1) not in visited_slots and (x, y + 1) not in region:
                    region.append((x, y + 1))

            total += area * boundary
    return total


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    data = ['.' + line + '.' for line in data]

    data = ['.' * len(data[0])] + data + ['.' * len(data[0])]

    result = calculate_area_and_boundary(data)

    print(result)


if __name__ == '__main__':
    main()
