import sys
import networkx as nx


def main():

    with open(sys.argv[1], 'r') as f:
        graph = {}
        data = f.readlines()
        data = [line.strip() for line in data]

        for line in data:
            # print(line)
            a, b = line.split(': ')
            if a not in graph:
                graph[a] = []

            for e in b.split(' '):
                if e not in graph:
                    graph[e] = []
                graph[a].append(e)
                graph[e].append(a)

        G = nx.Graph()

        for key, val in graph.items():
            for other in val:
                G.add_edge(key, other)
                G.add_edge(other, key)
        # print(graph)

        # print(data)
        # print(G)

        edges_to_remove = nx.minimum_edge_cut(G)
        # print(edges_to_remove)
        for edge in edges_to_remove:
            G.remove_edge(*edge)

        # print(G)

        connected_components = nx.connected_components(G)

        sizes = [len(c) for c in connected_components]
        print(sizes)

        total = sizes[0] * sizes[1]
        print(total)


if __name__ == '__main__':
    main()
