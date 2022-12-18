import sys


def is_interior(cube, cubes, min_x, max_x, min_y, max_y, min_z, max_z):

    x_left = False
    x_right = False

    y_left = False
    y_right = False

    z_left = False
    z_right = False

    for i in range(cube[0], max_x + 1):
        if (i, cube[1], cube[2]) in cubes:
            x_right = True
            break

    for i in range(min_x, cube[0] + 1):
        if (i, cube[1], cube[2]) in cubes:
            x_left = True
            break

    for i in range(cube[1], max_y + 1):
        if (cube[0], i, cube[2]) in cubes:
            y_right = True
            break

    for i in range(min_y, cube[1] + 1):
        if (cube[0], i, cube[2]) in cubes:
            y_left = True
            break

    for i in range(cube[2], max_z + 1):
        if (cube[0], cube[1], i) in cubes:
            z_right = True
            break

    for i in range(min_z, cube[2] + 1):
        if (cube[0], cube[1], i) in cubes:
            z_left = True
            break

    return (x_left and x_right and y_left and y_right and z_left and z_right and cube not in cubes)

def print_slice(cubes, middle_cube, min_x, max_x, min_y, max_y, z):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y, z) == middle_cube:
                print('@', end='')
            elif (x, y, z) in cubes:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

def show_cubes(cubes, middle_cube, min_x, max_x, min_y, max_y, min_z, max_z):
    for z in range(min_z, max_z + 1):
        print_slice(cubes, middle_cube, min_x, max_x, min_y, max_y, z)


def get_sides(cube):
    return [(cube[0] -1 , cube[1], cube[2]), (cube[0] + 1 , cube[1], cube[2]), (cube[0] , cube[1] - 1, cube[2]), (cube[0], cube[1] + 1, cube[2]), (cube[0], cube[1], cube[2] - 1), (cube[0], cube[1], cube[2] + 1)]
 
def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        cubes = set()
        all_cubes = []
        total_edges = 0
        min_x = 1000
        max_x = 0
        min_y = 1000
        max_y = 0
        min_z = 1000
        max_z = 0
        for row in data:
            row = tuple(list(map(int, row.split(','))))
            #print(row)
            cubes.add(row)
            all_cubes.append(row)
            if row[0] < min_x: min_x = row[0]
            if row[0] > max_x: max_x = row[0]
            if row[1] < min_y: min_y = row[1]
            if row[1] > max_y: max_y = row[1]
            if row[2] < min_z: min_z = row[2]
            if row[2] > max_z: max_z = row[2]

        middle_cube = ((min_x + max_x)//2, (min_y + max_y)//2, (min_z + max_z)//2)
        #middle_cube = (2, 2, 5)
        #print(middle_cube)
        #show_cubes(cubes, middle_cube, min_x, max_x, min_y, max_y, min_z, max_z)

        assert(True == is_interior(middle_cube, cubes, min_x, max_x, min_y, max_y, min_z, max_z))

        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                for k in range(min_z, max_z):
                    if is_interior((i, j, k), cubes, min_x, max_x, min_y, max_y, min_z, max_z):
                        #print(f'Found interior: {(i, j, k)}')
                        cubes.add((i, j, k))
                        all_cubes.append((i, j, k))
        #show_cubes(cubes, middle_cube, min_x, max_x, min_y, max_y, min_z, max_z)

        for cube in all_cubes:
            for side in get_sides(cube):
                if side not in cubes:
                    total_edges += 1
        #show_cubes(cubes, middle_cube, min_x, max_x, min_y, max_y, min_z, max_z)
        print(total_edges)

        

if __name__ == '__main__':
    main()
