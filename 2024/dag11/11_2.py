import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def _blink(stone, depth):
    if depth == 75:
        return 1

    str_stone = str(stone)
    if stone == 0:
        return _blink(1, depth + 1)
    elif len(str_stone) % 2 == 0:
        left_part = str_stone[:len(str_stone) // 2]
        right_part = str_stone[len(str_stone) // 2:]
        total = 0
        total += _blink(int(left_part), depth + 1)
        total += _blink(int(right_part), depth + 1)
        return total
    else:
        return _blink(2024 * stone, depth + 1)


def blink(stones):
    total = 0

    for stone in stones:
        total += _blink(stone, 0)
    return total


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [int(elem) for elem in data[0].split()]

    result = blink(data)
    print(result)


if __name__ == '__main__':
    main()
