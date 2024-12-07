import sys


def search(target: int, current: int, equation: list[int]):

    if not equation:
        return target == current

    equation_copy = [val for val in equation]
    val = equation_copy[0]
    equation_copy = equation_copy[1:]

    if search(target, current+val, equation_copy):
        return target
    if search(target, current*val, equation_copy):
        return target
    return 0


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [line.split(': ') for line in data]
        data = [[int(line[0]), list(map(int, line[1].split()))]
                for line in data]
        print(data)
        total = 0
        for eq in data:
            total += search(eq[0], 0, eq[1])
        print(total)


if __name__ == '__main__':
    main()
