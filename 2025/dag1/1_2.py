import sys


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [(elem[0], int(elem[1:])) for elem in data]
        # print(data)
    number = 50
    password = 0
    for dir, length in data:
        prev = number
        if dir == "R":
            for i in range(length):
                number += 1
                number %= 100
                if number == 0:
                    password += 1
        else:
            for i in range(length):
                number -= 1
                number %= 100
                if number == 0:
                    password += 1

    print(password)


if __name__ == "__main__":
    main()
