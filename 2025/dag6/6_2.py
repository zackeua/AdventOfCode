import sys
import re
import functools


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.replace("\n", "") for line in data]
        # print(data)
    operators = []
    for c in data[-1]:
        if c != " ":
            operators.append(c)
    # print(operators)
    problems = [[] for _ in operators]

    problem_index = 0
    for i, c in enumerate(data[0]):
        tmp_number = ""
        for j, line in enumerate(data[:-1]):
            tmp_number = tmp_number + data[j][i]
        if tmp_number.strip() != "":
            problems[problem_index].append(int(tmp_number))
        else:
            problem_index += 1

    # print(operators)
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
