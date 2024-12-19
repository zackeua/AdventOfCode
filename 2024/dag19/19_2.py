import sys
import tqdm
from functools import lru_cache


@lru_cache
def can_construct(pattern: str, avalible_towels: tuple[str]) -> bool:

    if pattern == '':
        return 1
    total = 0
    for towel in avalible_towels:

        position = pattern.find(towel)
        if position == 0:
            pattern_copy = pattern.replace(towel, '', 1)
            total += can_construct(pattern_copy, avalible_towels)

    return total


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [elem.strip() for elem in data]

    avalible_towels = data[0].split(', ')
    avalible_towels = tuple(avalible_towels)
    patterns = data[2:]

    total = 0
    for pattern in tqdm.tqdm(patterns):
        total += can_construct(pattern, avalible_towels)

    print(total)


if __name__ == '__main__':
    main()
