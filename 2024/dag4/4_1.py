import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

        total = 0
        for line in data:
            for i, elem in enumerate(line):
                word = line[i:i+4]
                if word in ('XMAS', 'SAMX'):
                    total += 1

        for i, line in enumerate(data):
            for j, elem in enumerate(line):
                if i + 4 <= len(data) and j + 4 < len(line):
                    word = ''.join([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]])
                    if word in ('XMAS', 'SAMX'):
                        total += 1
                if i + 4 <= len(data) and j - 4 < len(line):
                    word = ''.join([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]])
                    if word in ('XMAS', 'SAMX'):
                        total += 1
        for j, elem in enumerate(data[0]):
            for i , line in enumerate(data):
                if i + 4 <= len(data):
                    word = ''.join([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]])
                    if word in ('XMAS', 'SAMX'):
                        total += 1
        print(total)


if __name__ == '__main__':
    main()
