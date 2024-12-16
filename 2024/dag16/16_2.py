import sys
import networkx as nx


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = data[::-1]

    # print(data)
    start_node = None
    end_node = (-1, -1)
    graph = nx.DiGraph()
    for i in range(1, len(data)):
        for j in range(1, len(data[0])):
            elem = data[i][j]
            if elem != '#':
                if elem == 'S':
                    start_node = (i, j, 0, 1)
                if elem == 'E':
                    # print('end')
                    graph.add_edge((i, j, 1, 0), end_node, weight=0)
                    graph.add_edge((i, j, 0, 1), end_node, weight=0)
                    graph.add_edge((i, j, -1, 0), end_node, weight=0)
                    graph.add_edge((i, j, 0, -1), end_node, weight=0)
                if data[i][j - 1] != '#':
                    graph.add_edge((i, j - 1, 0, 1), (i, j, 0, 1), weight=1)
                    graph.add_edge((i, j, 0, -1), (i, j - 1, 0, -1), weight=1)
                if data[i][j + 1] != '#':
                    graph.add_edge((i, j + 1, 0, -1), (i, j, 0, -1), weight=1)
                    graph.add_edge((i, j, 0, 1), (i, j + 1, 0, 1), weight=1)
                if data[i - 1][j] != '#':
                    graph.add_edge((i - 1, j, 1, 0), (i, j, 1, 0), weight=1)
                    graph.add_edge((i, j, -1, 0), (i - 1, j, -1, 0), weight=1)
                if data[i + 1][j] != '#':
                    graph.add_edge((i, j, 1, 0), (i + 1, j, 1, 0), weight=1)
                    graph.add_edge((i + 1, j, -1, 0), (i, j, -1, 0), weight=1)

                graph.add_edge((i, j, 1, 0), (i, j, 0, 1), weight=1000)
                graph.add_edge((i, j, 0, 1), (i, j, 1, 0), weight=1000)

                graph.add_edge((i, j, 0, 1), (i, j, -1, 0), weight=1000)
                graph.add_edge((i, j, -1, 0), (i, j, 0, 1), weight=1000)

                graph.add_edge((i, j, -1, 0), (i, j, 0, -1), weight=1000)
                graph.add_edge((i, j, 0, -1), (i, j, -1, 0), weight=1000)

                graph.add_edge((i, j, 0, -1), (i, j, 1, 0), weight=1000)
                graph.add_edge((i, j, 1, 0), (i, j, 0, -1), weight=1000)

    # distance = nx.dijkstra_path_length(graph, start_node, end_node)
    result = nx.all_shortest_paths(graph, start_node, end_node)
    nodes = []
    for path in result:
        for elem in path:
            if (elem[0], elem[1]) not in nodes:
                nodes.append((elem[0], elem[1]))

    total = len(nodes) - 1
    print(total)
    assert total < 602


if __name__ == '__main__':
    main()
