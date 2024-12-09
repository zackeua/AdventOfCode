import sys


def print_disk_map(disk_map):

    disk_map_copy = ['.' if elem == None else str(elem) for elem in disk_map]

    print(''.join(disk_map_copy))


def calculate_checksum(disk_map):
    i = 0
    total = 0
    while disk_map[i] is not None:
        total += i * disk_map[i]
        i += 1
    return total


def move_files(disk_map: list[int]):
    empty_pos = disk_map.index(None)
    pos_to_move = len(disk_map) - 1
    while disk_map[pos_to_move] is None:
        pos_to_move -= 1

    while empty_pos >= 0 and empty_pos <= pos_to_move:
        disk_map[empty_pos] = disk_map[pos_to_move]
        disk_map[pos_to_move] = None
        empty_pos = disk_map.index(None)
        while disk_map[pos_to_move] is None:
            pos_to_move -= 1

    return disk_map


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = data[0].strip()
        disk_map = []
        for i, elem in enumerate(data):
            for _ in range(int(elem)):
                if i % 2 == 0:
                    disk_map.append(i//2)
                else:
                    disk_map.append(None)
        # print_disk_map(disk_map)
        disk_map = move_files(disk_map)
        # print_disk_map(disk_map)

        result = calculate_checksum(disk_map)
        print(result)


if __name__ == '__main__':
    main()
