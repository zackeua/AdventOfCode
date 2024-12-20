import sys
import networkx as nx
import tqdm


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    graph = nx.DiGraph()
    start = None
    end = None
    for i, line in enumerate(data):
        for j, elem in enumerate(line):
            if elem == '#':
                continue

            if elem == 'S':
                start = (i, j)

            if elem == 'E':
                end = (i, j)

            if data[i + 1][j] != '#':
                graph.add_edge((i, j), (i + 1, j))
                graph.add_edge((i + 1, j), (i, j))
            if data[i - 1][j] != '#':
                graph.add_edge((i, j), (i - 1, j))
                graph.add_edge((i - 1, j), (i, j))

            if data[i][j + 1] != '#':
                graph.add_edge((i, j), (i, j + 1))
                graph.add_edge((i, j + 1), (i, j))
            if data[i][j - 1] != '#':
                graph.add_edge((i, j), (i, j - 1))
                graph.add_edge((i, j - 1), (i, j))

    baseline_distance = nx.dijkstra_path_length(graph, start, end)

    # print(baseline_distance)

    buckets = {}
    for i, line in enumerate(tqdm.tqdm(data)):
        for j, elem in enumerate(line):
            for d_i, d_j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if elem != '#':
                    continue
                if i + d_i < 0:
                    continue
                if j + d_i < 0:
                    continue
                if i + d_i >= len(data):
                    continue
                if j + d_j >= len(data[0]):
                    continue
                graph_copy = graph.copy()

                graph_copy.add_edge((i - d_i, j - d_j), (i, j))
                graph_copy.add_edge((i, j), (i - d_i, j - d_j))
                graph_copy.add_edge((i + d_i, j + d_j), (i, j))
                graph_copy.add_edge((i, j), (i + d_i, j + d_j))

                new_distance = nx.dijkstra_path_length(graph_copy, start, end)
                if new_distance < baseline_distance:
                    saved = baseline_distance - new_distance
                    if saved not in buckets:
                        buckets[saved] = 0
                    buckets[saved] += 1
    total = 0
    for key in buckets.keys():
        # print(key, ' ', buckets[key])
        if key >= 100:
            total += buckets[key] // 2

    print(total)


if __name__ == '__main__':
    main()
