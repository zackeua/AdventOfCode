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

    distances_from_start = nx.single_source_dijkstra(graph, start)[0]
    distances_from_end = nx.single_source_dijkstra(graph, end)[0]

    total = 0
    buckets = {}
    for i, j in distances_from_start.keys():
        old_distance = distances_from_start[(i, j)] + distances_from_end[(i, j)]

        for i_d in range(-20, 21):
            for j_d in range(-20, 21):
                if abs(i_d) + abs(j_d) > 20:
                    continue
                new_distance = distances_from_start[(i, j)] + abs(i_d) + abs(j_d) + distances_from_end.get((i + i_d, j + j_d), distances_from_end[start])
                saved = old_distance - new_distance

                if 0 < saved:
                    if saved not in buckets:
                        buckets[saved] = 0
                    buckets[saved] += 1

                if saved >= 100:
                    total += 1

    for key in buckets.keys():
        if key >= 50:
            # print(buckets[key], key)
            pass

    print(total)
    assert total > 643301


if __name__ == '__main__':
    main()
