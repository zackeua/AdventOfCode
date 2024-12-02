import sys

def increasing(line):
    prev = None
    if line[0] < line[1]:
        for elem in line:
            if prev is not None:
                if prev > elem:
                    return False

            prev = elem
    else:
        for elem in line:
            if prev is not None:
                if prev < elem:
                    return False

            prev = elem
    return True


def differ(line):
    prev = None
    for elem in line:
        if prev is not None:
            diff = abs(prev - elem)
            if not(1 <= diff <= 3):
                return False

        prev = elem
    return True



def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [list(map(int, row.split())) for row in data]

        total = 0

        for line in data:
            if increasing(line) and differ(line):
                total += 1
        print(total)


if __name__ == '__main__':
    main()
