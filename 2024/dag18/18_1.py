import sys
import networkx as nx


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [tuple(map(int, line.strip().split(','))) for line in data]
        # print(data)

    blocked_spaces = data[:1024]
    for i in range(0, 70):
        blocked_spaces.append((-1, i))
        blocked_spaces.append((71, i))
        blocked_spaces.append((i, -1))
        blocked_spaces.append((i, 71))

    blocked_spaces = set(blocked_spaces)
    # print(blocked_spaces)
    graph = nx.DiGraph()
    for i in range(0, 71):
        for j in range(0, 71):
            if (i, j) in blocked_spaces:
                continue

            if (i - 1, j) not in blocked_spaces:
                graph.add_edge((i, j), (i-1, j))
            if (i + 1, j) not in blocked_spaces:
                graph.add_edge((i, j), (i+1, j))
            if (i, j - 1) not in blocked_spaces:
                graph.add_edge((i, j), (i, j-1))
            if (i, j + 1) not in blocked_spaces:
                graph.add_edge((i, j), (i, j+1))

    distance = nx.shortest_path_length(graph, (0, 0), (70, 70))
    print(distance)


if __name__ == '__main__':
    main()
