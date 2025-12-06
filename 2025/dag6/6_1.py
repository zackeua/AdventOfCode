import sys
import re
import functools


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        # print(data)
    operators = []
    for c in data[-1]:
        if c != " ":
            operators.append(c)
    # print(operators)
    problems = [[] for _ in operators]
    for line in data[:-1]:
        matches = re.findall(r"(\d+)", line)
        # print(matches)
        for i, elem in enumerate(matches):
            problems[i].append(int(elem))
    # print(problems)

    total = 0
    for i, op in enumerate(operators):
        if op == "+":
            ans = sum(problems[i])
        elif op == "*":
            ans = functools.reduce(lambda x, y: x * y, problems[i], 1)
        total += ans
    print(total)


if __name__ == "__main__":
    main()
