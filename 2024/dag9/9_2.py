import sys


class File:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end

    def __str__(self):
        if self.id is None:
            id = '.'
        else:
            id = str(self.id)

        return id * (self.end - self.start)


def print_disk_map(disk_map):

    disk_map_copy = [str(elem) for elem in disk_map]

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
            if i % 2 == 0:
                disk_map.append(File(i//2, i, i + int(elem)))
            else:
                disk_map.append(File(None, i, i + int(elem)))
        print_disk_map(disk_map)
        # disk_map = move_files(disk_map)
        # print_disk_map(disk_map)

        # result = calculate_checksum(disk_map)
        # print(result)


if __name__ == '__main__':
    main()
