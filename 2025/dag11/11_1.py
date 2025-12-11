import sys


def search(start, target, graph):
    if start == target:
        return 1
    total = 0
    for node in graph[start]:
        total += search(node, target, graph)
    return total


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [line.split(": ") for line in data]
        edges = {key: tuple(values.split(" ")) for key, values in data}
        # print(edges)
    total = search("you", "out", edges)
    print(total)


if __name__ == "__main__":
    main()
