import sys


def determine_sides(garden, boundary_elements):
    total_sides = 0
    visited = []
    elements = [elem for elem in boundary_elements]

    while elements:
        element = elements[0]
        elements = elements[1:]
        visited.append(element)
        total_sides += 1
        x, y = element

        if (x - 1, y) in elements:
            elements.remove((x - 1, y))
        if (x + 1, y) in elements:
            elements.remove((x + 1, y))
        if (x, y - 1) in elements:
            elements.remove((x, y - 1))
        if (x, y + 1) in elements:
            elements.remove((x, y + 1))

    return visited


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
            boundary_elements = set()
            corners = 0
            convex = 0

            while region:
                (x, y) = region[0]
                region = region[1:]

                elem = garden[x][y]
                area += 1

                visited_slots.add(((x, y)))
                tmp_sides = 0

                if garden[x - 1][y] != elem:
                    pass
                elif (x - 1, y) not in visited_slots and (x - 1, y) not in region:
                    region.append((x - 1, y))

                if garden[x + 1][y] != elem:
                    pass
                elif (x + 1, y) not in visited_slots and (x + 1, y) not in region:
                    region.append((x + 1, y))

                if garden[x][y - 1] != elem:
                    pass
                elif (x, y - 1) not in visited_slots and (x, y - 1) not in region:
                    region.append((x, y - 1))

                if garden[x][y + 1] != elem:
                    pass
                elif (x, y + 1) not in visited_slots and (x, y + 1) not in region:
                    region.append((x, y + 1))

                # check concave corners
                if garden[x][y] == elem and garden[x][y + 1] == elem and garden[x + 1][y] == elem and garden[x + 1][y + 1] != elem:
                    corners += 1

                if garden[x][y] == elem and garden[x][y - 1] == elem and garden[x + 1][y] == elem and garden[x + 1][y - 1] != elem:
                    corners += 1

                if garden[x][y] == elem and garden[x][y - 1] == elem and garden[x - 1][y] == elem and garden[x - 1][y - 1] != elem:
                    corners += 1

                if garden[x][y] == elem and garden[x][y + 1] == elem and garden[x - 1][y] == elem and garden[x - 1][y + 1] != elem:
                    corners += 1

                # check convex corners
                if garden[x][y] == elem and garden[x - 1][y] != elem and garden[x][y - 1] != elem:
                    corners += 1

                if garden[x][y] == elem and garden[x + 1][y] != elem and garden[x][y - 1] != elem:
                    corners += 1

                if garden[x][y] == elem and garden[x - 1][y] != elem and garden[x][y + 1] != elem:
                    corners += 1

                if garden[x][y] == elem and garden[x + 1][y] != elem and garden[x][y + 1] != elem:
                    corners += 1

            sides = corners
            total += area * sides
    return total


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    data = ['.' + line + '.' for line in data]

    data = ['.' * len(data[0])] + data + ['.' * len(data[0])]

    result = calculate_area_and_boundary(data)

    print(result)
    assert result > 813785


if __name__ == '__main__':
    main()
