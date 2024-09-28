import sys
import pdb


def _print(a, **kwargs):
    if False:
        print(a, **kwargs)


class Graph:

    def __init__(self):
        self._adj_matrix = {}

    def add_edge(self, u, v, weight=1):
        ''''''
        if u not in self._adj_matrix:
            self._adj_matrix[u] = {}
        if v not in self._adj_matrix:
            self._adj_matrix[v] = {}

        # assert u in self._adj_matrix[v], f'{u} is not in Graph'
        # assert v in self._adj_matrix[u], f'{v} is not in Graph'

        self._adj_matrix[u][v] = weight
        self._adj_matrix[v][u] = weight

    def remove_node(self, u):
        if u in self._adj_matrix:
            del self._adj_matrix[u]
        for elem in self._adj_matrix:
            if u in elem:
                del elem[u]

    def get_neighbors(self, u):
        assert u in self._adj_matrix, f'{u} is not in Graph'
        return self._adj_matrix[u].keys()

    def add_node(self, u):
        assert u not in self._adj_matrix, f'{u} is already in Graph'
        self._adj_matrix[u] = {}

    def get_nodes(self):
        return self._adj_matrix.keys()

    def get_edges(self):
        result = []
        for fr, val in self._adj_matrix.items():
            for to, elem in val.items():
                result.append((fr, to, elem))

        return result

    def __contains__(self, u):
        return u in self._adj_matrix

    def codense_graph(self):
        condense = True

        while condense:
            condense = False
            keys = list(self._adj_matrix.keys())
            for node in keys:
                neighbors = list(self._adj_matrix[node].keys())
                if len(neighbors) == 2:
                    condense = True
                    total_weight = self._adj_matrix[node][neighbors[0]] \
                        + self._adj_matrix[node][neighbors[1]]
                    del self._adj_matrix[node]
                    self._adj_matrix[neighbors[0]][neighbors[1]] = total_weight
                    self._adj_matrix[neighbors[1]][neighbors[0]] = total_weight

    def get_weight(self, u, v):
        return self._adj_matrix[u][v]


def get_neighbors_in_input(graph, node):
    neighbors = []

    if graph[node[0] - 1][node[1]] not in '#':
        neighbors.append((node[0] - 1, node[1]))

    if graph[node[0] + 1][node[1]] not in '#':
        neighbors.append((node[0] + 1, node[1]))

    if graph[node[0]][node[1] - 1] not in '#':
        neighbors.append((node[0], node[1] - 1))

    if graph[node[0]][node[1] + 1] not in '#':
        neighbors.append((node[0], node[1] + 1))

    return neighbors


def is_node(graph, node):
    if graph[node[0]][node[1]] == '#':
        return False

    count = 0
    if graph[node[0] - 1][node[1]] not in '#':
        count += 1

    if graph[node[0] + 1][node[1]] not in '#':
        count += 1

    if graph[node[0]][node[1] - 1] not in '#':
        count += 1

    if graph[node[0]][node[1] + 1] not in '#':
        count += 1

    # is node if there is at least
    return count > 2


def modify_input_data(data, start, target):
    new_data = []

    for line in data:
        new_line = ['#' if elem == '#' else '.' for elem in line]
        new_data.append(new_line)

    new_data[start[0]][start[1]] = '*'
    new_data[target[0]][target[1]] = '*'

    nodes = [start, target]

    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            if is_node(data, (row, col)):
                new_data[row][col] = '*'
                nodes.append((row, col))

    return new_data, nodes


def create_graph(data, start: tuple, goal: tuple):

    modified_data, nodes = modify_input_data(data, start, goal)

    for line in modified_data:
        print(''.join(line))

    graph = Graph()

    for node in nodes:
        graph.add_node(node)

    graph_node_len = len(graph.get_nodes())

    for start_node in nodes:
        to_visit = []
        to_visit.append((start_node, start_node, 0))  # source current distance
        visited = []

        while to_visit:
            source_node, current_node, distance = to_visit[0]
            to_visit = to_visit[1:]

            if current_node not in visited:
                visited.append(current_node)

            if current_node in graph.get_nodes() and current_node != source_node:
                graph.add_edge(source_node, current_node, distance)
            else:
                neighbors = get_neighbors_in_input(data, current_node)
                for n in neighbors:
                    if n not in visited:
                        to_visit.append((source_node, n, distance + 1))

    return graph


def search(graph: Graph, start, goal, visited=None):

    if visited is None:
        visited = [start]
    result_visited = [e for e in visited]
    outer_result = 0
    for node in graph.get_neighbors(start):
        if node == goal:
            return graph.get_weight(start, goal), visited + [goal]
        if node not in visited:
            local_visited = visited + [node]
            local_result, local_visited = search(
                graph, node, goal, local_visited)
            local_result += graph.get_weight(start, node)
            if local_result > outer_result:
                outer_result = local_result
                result_visited = local_visited

    return outer_result, result_visited


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        data = ['#' * len(data[0])] + data + ['#' * len(data[0])]
    start = (1, 1)
    goal = (len(data) - 2, len(data[0]) - 2)

    graph = create_graph(data, start, goal)

    result, visited = search(graph, start, goal)
    # result -= 2
    print(result)
    print(len(graph.get_nodes()))
    print(len(graph.get_edges()))
    # result = 0
    assert result > 1798
    assert result > 6382
    assert result > 6448
    assert result != 6414
    assert result != 6450
    assert result != 6495


if __name__ == '__main__':
    main()
