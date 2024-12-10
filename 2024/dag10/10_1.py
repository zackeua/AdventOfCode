import sys


def intenal_search(data, current_val, i, j):
    if current_val == 9:
        return set([(i, j)])
    total = set()
    if data[i - 1][j] == current_val + 1:
        total |= intenal_search(data, current_val + 1, i - 1, j)
    if data[i + 1][j] == current_val + 1:
        total |= intenal_search(data, current_val + 1, i + 1, j)
    if data[i][j - 1] == current_val + 1:
        total |= intenal_search(data, current_val + 1, i, j - 1)
    if data[i][j + 1] == current_val + 1:
        total |= intenal_search(data, current_val + 1, i, j + 1)
    return total


def search(data, current_val):
    total = 0
    for i, line in enumerate(data):
        for j, elem in enumerate(line):
            if elem == 0:
                tailhad_count = intenal_search(data, 0, i, j)
                # print(tailhad_count)
                # print(len(tailhad_count))
                total += len(tailhad_count)
    return total


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    data = [[-1] + list(map(int, line)) + [-1] for line in data]
    data = [[-1] * len(data[0])] + data + [[-1] * len(data[0])]

    result = search(data, 0)

    print(result)


if __name__ == '__main__':
    main()
