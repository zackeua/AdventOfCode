import sys
import itertools
from collections import deque


def groupwise(iterable, n):
    accum = deque((), n)
    for element in iterable:
        accum.append(element)
        if len(accum) == n:
            yield tuple(accum)


def calculate_secret_number(number):

    # step 1:
    n = (number * 64)
    n = number ^ n
    n = n % 16777216

    # step 2:
    m = n // 32
    n = n ^ m
    n = n % 16777216

    # step 3:
    m = n * 2048
    n = n ^ m
    n = n % 16777216
    return n


def is_valid_sequence(sequence):
    if not (-9 <= sum(sequence) <= 9):
        return False
    if not (-9 <= sequence[0] + sequence[1] <= 9):
        return False

    if not (-9 <= sequence[1] + sequence[2] <= 9):
        return False

    if not (-9 <= sequence[2] + sequence[3] <= 9):
        return False

    return True


def search(all_prices, all_differences):
    most_bananas = 0

    all_sequences = itertools.permutations(range(-9, 10), 4)
    # all_sequences = [(-2, 1, -1, 3)]
    for sequence in all_sequences:
        if not is_valid_sequence(sequence):
            continue
        # print(sequence)
        total = 0
        for i, differences in enumerate(all_differences):
            total += all_differences[i].get(sequence, 0)

        if total > most_bananas:
            most_bananas = total

    return most_bananas


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [int(line.strip()) for line in data]

    all_prices = []
    all_differences = []
    all_differences_lookup = []
    for number in data:
        i = 0
        prices = []
        differences = []
        secret = number
        prices.append(secret % 10)
        # print(f'{secret}: {prices[-1]}')
        while i < 2000:  # 10:  # 2000:
            secret = calculate_secret_number(secret)
            prices.append(secret % 10)
            difference = prices[-1] - prices[-2]
            i += 1
            # print(f'{secret}: {prices[-1]} ({difference})')
            differences.append(difference)
        all_prices.append(prices)
        all_differences.append(differences)

    for i, differences in enumerate(all_differences):
        differences_lookup = {}
        for j, difference_sequence in enumerate(groupwise(differences, 4), start=4):
            if difference_sequence not in differences_lookup:
                differences_lookup[difference_sequence] = all_prices[i][j]
        all_differences_lookup.append(differences_lookup)

    most = search(all_prices, all_differences_lookup)
    print(most)
    assert most > 1855


if __name__ == '__main__':
    main()
