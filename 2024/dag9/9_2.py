import sys


class File:
    def __init__(self, id, start, length):
        self.id = id
        self.start = start
        self.length = length

    def __str__(self):
        if self.id is None:
            id = '.'
        else:
            id = str(self.id)

        return id * self.length


def replace_empty_file(moved_file: File, empty_file: File):
    assert moved_file.id is not None
    assert empty_file.id is None
    assert moved_file.length <= empty_file.length

    if moved_file.id == 9:
        print(moved_file.length)
        input()
    new_file = File(moved_file.id, empty_file.start, moved_file.length)
    new_empty_file_length = empty_file.length - new_file.length
    if new_empty_file_length == 0:
        return new_file, None
    assert new_empty_file_length > 0
    new_empty_file_start = empty_file.start + moved_file.length
    new_empty_file = File(None, new_empty_file_start, new_empty_file_length)

    return new_file, new_empty_file


def merge_empty_files(file1: File, file2: File, file3: File):
    start_of_interval = file2.start
    length_of_interval = file2.length
    if file1.id is None and file2.id is None and file3.id is None:
        start_of_interval = file1.start
        length_of_interval = file1.length + file2.length + file3.length
        return File(None, start_of_interval, length_of_interval), None, None
    if file1.id is None and file2.id is None:
        start_of_interval = file1.start
        length_of_interval = file1.length + file2.length
        return File(None, start_of_interval, length_of_interval), None, file3
    if file2.id is None and file3.id is None:
        start_of_interval = file2.start
        length_of_interval = file2.length + file3.length
        return file1, File(None, start_of_interval, length_of_interval), None
    return file1, file2, file3


def print_disk_map(disk_map):

    disk_map_copy = [str(elem) for elem in disk_map]

    print(''.join(disk_map_copy))


def calculate_checksum(disk_map: list[File]):
    total = 0
    for file in disk_map:
        print(file.id, file.start, file.length)
        if file.id is not None:
            for i in range(file.start, file.start + file.length):
                total += i * file.id

    return total


def move_files(disk_map: list[File]):
    max_file_id = disk_map[-2].id
    files_to_iterate = range(max_file_id, -1, -1)  # from largest to 0

    for file_id in files_to_iterate:
        max_file_pos_to_consider = 0
        while disk_map[max_file_pos_to_consider].id != file_id:
            max_file_pos_to_consider += 1

        file_to_move = disk_map[max_file_pos_to_consider]
        moved_file = None
        new_empty_space = None
        for file_position in range(0, max_file_pos_to_consider):
            position_to_consider = disk_map[file_position]
            if position_to_consider.id is not None:
                continue
            if position_to_consider.length < file_to_move.length:
                continue
            moved_file, new_empty_space = replace_empty_file(
                file_to_move, position_to_consider)
            break
        if moved_file is None:
            continue

        disk_map[file_position] = moved_file
        disk_map[max_file_pos_to_consider].id = None
        f1 = disk_map[max_file_pos_to_consider - 1]
        f2 = disk_map[max_file_pos_to_consider]
        f3 = disk_map[max_file_pos_to_consider + 1]
        file1, file2, file3 = merge_empty_files(f1, f2, f3)
        if file3 is None:
            disk_map.remove(f3)
        else:
            disk_map[max_file_pos_to_consider + 1] = file3
        if file2 is None:
            disk_map.remove(f2)
        else:
            disk_map[max_file_pos_to_consider] = file2
        if file1 is None:
            disk_map.remove(f1)
        else:
            disk_map[max_file_pos_to_consider - 1] = file1

        if new_empty_space is not None:
            disk_map.insert(file_position + 1, new_empty_space)

    return disk_map


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = data[0].strip()
        disk_map = []
        start_id = 0
        for i, elem in enumerate(data):
            file_id = None
            if i % 2 == 0:
                file_id = i // 2
            file_len = int(elem)
            if file_len != 0:
                disk_map.append(File(file_id, start_id, file_len))
            start_id += file_len
        disk_map.append(File(None, start_id, 1))
        print_disk_map(disk_map)
        calculate_checksum(disk_map)
        disk_map = move_files(disk_map)
        print_disk_map(disk_map)

        result = calculate_checksum(disk_map)
        print(result)
        assert result < 6511180698509


if __name__ == '__main__':
    main()
