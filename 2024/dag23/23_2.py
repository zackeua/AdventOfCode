import sys
import itertools
import networkx as nx


class Graph:
    def __init__(self):
        self._nodes = []
        self._neighbors = {}

    def add_node(self, node):
        if node not in self._nodes:
            self._nodes.append(node)

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        if node1 not in self._neighbors:
            self._neighbors[node1] = []
        self._neighbors[node1].append(node2)

        if node2 not in self._neighbors:
            self._neighbors[node2] = []
        self._neighbors[node2].append(node1)

    def get_nodes(self):
        return self._nodes

    def get_neighbors(self, node):
        if node not in self._neighbors:
            return []

        return self._neighbors[node]


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    graph = nx.Graph()
    for line in data:
        n1, n2 = line.split('-')
        graph.add_edge(n1, n2)

    largest_len = 0
    largest = []

    cleques = nx.find_cliques(graph)
    for c in cleques:
        if len(c) > largest_len:
            largest = c
            largest_len = len(c)

    largest = sorted(largest)
    print(','.join(largest))


if __name__ == '__main__':
    main()
