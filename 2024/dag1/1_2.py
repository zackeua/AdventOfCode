import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        first_list = []
        second_dict = {} 
        for row in data:
            first, second = list(map(int, row.split()))
            first_list.append(first)
            if second not in second_dict:
                second_dict[second] = 0
            second_dict[second] += 1

        first_list.sort()

        result = 0
        for first in first_list:
            result += first * second_dict.get(first, 0)
        print(result)
            



if __name__ == '__main__':
    main()
