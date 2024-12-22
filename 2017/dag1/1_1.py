import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = data[0]

        total = 0
        for i in range(len(data)):
            # print(i)
            if i == len(data) - 1:
                if data[i] == data[0]:
                    total = total + int(data[i])

            elif data[i] == data[i + 1]:
                total = total + int(data[i])
        print(total)


if __name__ == '__main__':
    main()
