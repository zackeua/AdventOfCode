import sys
import re


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = data[0].strip().split(",")
        data = [elem.split("-") for elem in data]
        # print(data)
    total = 0
    for elem in data:
        lower_bound = int(elem[0])
        upper_bound = int(elem[1])
        for i in range(lower_bound, upper_bound):
            i_s = str(i)
            matching = re.match(r"^([1-9]\d*)\1$", i_s)
            if matching is not None:
                total += i
                # print(i)
    print(total)


if __name__ == "__main__":
    main()
