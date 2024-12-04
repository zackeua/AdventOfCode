import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

        total = 0

        for i, line in enumerate(data):
            for j, elem in enumerate(line):
                if i + 3 <= len(data) and j + 3 < len(line):
                    word = ''.join([data[i][j], data[i+1][j+1], data[i+2][j+2]])
                    word2 = ''.join([data[i+2][j], data[i+1][j+1], data[i][j+2]])
                    if word in ('MAS', 'SAM') and word2 in ('MAS', 'SAM'):
                        total += 1

        print(total)


if __name__ == '__main__':
    main()
