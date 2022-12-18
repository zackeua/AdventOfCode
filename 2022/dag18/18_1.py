import sys


def get_sides(cube):
    return [(cube[0] -1 , cube[1], cube[2]), (cube[0] + 1 , cube[1], cube[2]), (cube[0] , cube[1] - 1, cube[2]), (cube[0], cube[1] + 1, cube[2]), (cube[0], cube[1], cube[2] - 1), (cube[0], cube[1], cube[2] + 1)]

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        cubes = set()
        total_edges = 0
        all_cubes = []
        for row in data:
            row = tuple(list(map(int, row.split(','))))
            #print(row)
            cubes.add(row)
            all_cubes.append(row)
        for cube in all_cubes:
            for side in get_sides(cube):
                if side not in cubes:
                    total_edges += 1
        print(total_edges)

        

if __name__ == '__main__':
    main()
