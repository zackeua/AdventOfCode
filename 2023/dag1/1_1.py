import sys



def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        total = 0
        for line in data:
            number = ''
            for elem in line:
                if elem in '0123456789':
                    number += elem
                    break
            for elem in line[::-1]:
                if elem in '0123456789':
                    number += elem
                    break
            total += int(number)
        print(total)


if __name__ == '__main__':
    main()