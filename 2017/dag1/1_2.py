import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = data[0]

        total = 0
        for i in range(len(data)):
            if data[i] == data[(i + len(data)//2) % len(data)]:
                total += int(data[i])
        print(total)


if __name__ == '__main__':
    main()
