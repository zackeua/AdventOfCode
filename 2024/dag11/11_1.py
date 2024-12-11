import sys


def blink(stones):
    new_stones = []
    for stone in stones:
        str_stone = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(str_stone) % 2 == 0:
            left_part = str_stone[:len(str_stone) // 2]
            right_part = str_stone[len(str_stone) // 2:]
            new_stones.append(int(left_part))
            new_stones.append(int(right_part))
        else:
            new_stones.append(2024 * stone)
    return new_stones


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [int(elem) for elem in data[0].split()]
    # print(data)

    for _ in range(25):
        data = blink(data)
        # print(data)
    print(len(data))


if __name__ == '__main__':
    main()
