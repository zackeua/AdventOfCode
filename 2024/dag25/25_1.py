import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data.append('')

    keys = []
    locks = []

    reading = [0, 0, 0, 0, 0]

    is_lock = False

    for i, line in enumerate(data):
        if line == '':
            if is_lock:
                locks.append(reading)
            else:
                keys.append(reading)
            is_lock = False
            reading = [0, 0, 0, 0, 0]
        else:
            if i % 8 == 0:
                if line == '#####':
                    is_lock = True
                else:
                    is_lock = False
            for j, elem in enumerate(line):
                reading[j] += elem == '#'

    # print(data)
    # print(keys)
    # print(locks)
    total = 0
    for lock in locks:
        for key in keys:
            total_sum = [a+b <= 7 for a, b in zip(key, lock)]
            fits = all(total_sum)
            # print(lock, ' ', key, ' ', fits)
            if fits:
                total += 1
    print(total)


if __name__ == '__main__':
    main()
