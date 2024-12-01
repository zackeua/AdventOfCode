import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        first_list = []
        second_list = []
        for row in data:
            first, second = list(map(int, row.split()))
            first_list.append(first)
            second_list.append(second)

        first_list.sort()
        second_list.sort()

        result = 0
        for first, second in zip(first_list, second_list):
            result += abs(first - second)
        print(result)
            



if __name__ == '__main__':
    main()
