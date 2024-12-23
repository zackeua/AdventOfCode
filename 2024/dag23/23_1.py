import sys
import itertools


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

    graph = Graph()
    for line in data:
        n1, n2 = line.split('-')
        graph.add_edge(n1, n2)

    total = 0
    for group_3 in itertools.combinations(graph.get_nodes(), 3):
        n1, n2, n3 = group_3
        if not (n1[0] == 't' or n2[0] == 't' or n3[0] == 't'):
            continue

        nn1 = graph.get_neighbors(n1)
        nn2 = graph.get_neighbors(n2)
        nn3 = graph.get_neighbors(n3)
        is_inter_connected = True
        if n2 not in nn1 or n3 not in nn1:
            is_inter_connected = False
        if n1 not in nn2 or n3 not in nn2:
            is_inter_connected = False
        if n1 not in nn3 or n2 not in nn3:
            is_inter_connected = False
        if is_inter_connected:
            total += 1
    print(total)


if __name__ == '__main__':
    main()
