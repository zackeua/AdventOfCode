import sys


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [(elem[0], int(elem[1:])) for elem in data]
        # print(data)
    number = 50
    password = 0
    for dir, length in data:
        if dir == "R":
            number += length
        else:
            number -= length
        number %= 100
        # print(number)
        if number == 0:
            password += 1
    print(password)


if __name__ == "__main__":
    main()
