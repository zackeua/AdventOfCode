import sys
import dataclasses
import heapq


@dataclasses.dataclass
class Node:
    distance: int = 0
    x: int = 0
    y: int = 0
    current_x: int = 0
    current_y: int = 0

    def __init__(self, x=0, y=0, current_x=0, current_y=0, distance=0):
        self.x = x
        self.y = y
        self.current_x = current_x
        self.current_y = current_y
        self.distance = distance

    def __add__(self, other):
        next_x = self.x + other.x
        next_y = self.y + other.y
        if next_x < self.x:
            c_x = self.current_x - 1
        elif next_x > self.x:
            c_x = self.current_x + 1
        elif next_x == self.x:
            c_x = 0

        if next_y < self.y:
            c_y = self.current_y - 1
        elif next_y > self.y:
            c_y = self.current_y + 1
        elif next_y == self.y:
            c_y = 0

        return Node(x=next_x,
                    y=next_y,
                    current_x=c_x,
                    current_y=c_y,
                    distance=self.distance + other.distance)

    def __lt__(self, other):
        return (self.distance, self.x, self.y, self.current_x + self.current_y) < (other.distance, other.x, other.y, other.current_x + other.current_y)

    def __eq__(self, other):
        return (self.x, self.y, self.current_x, self.current_y, self.distance) == (other.x, other.y, other.current_x, other.current_y, other.distance)

    def __hash__(self):
        return hash((self.x, self.y, self.current_x, self.current_y))

def print_history(history, node, graph):
    
    nodes = []
    nodes.append(node)
    while node in history:
        node = history[node]
        nodes.append(node)
    
    for x, row in enumerate(graph):
        for y, elem in enumerate(row):
            printed = False
            for node in nodes:
                if node.x == x and node.y == y:
                    print('X', end='')
                    printed = True
                    break
            if not printed:
                print(elem, end='')
        print()




def get_neighbors(graph, node):
    up_weight = graph[node.x - 1][node.y] if node.x - 1 >= 0 else sys.float_info.max
    down_weight = graph[node.x + 1][node.y] if node.x + 1 < len(graph) else sys.float_info.max
    left_weight = graph[node.x][node.y - 1] if node.y - 1 >= 0 else sys.float_info.max
    right_weight = graph[node.x][node.y + 1] if node.y + 1 < len(graph[0]) else sys.float_info.max

    UP = node + Node(x=-1, y=0, distance=up_weight)
    DOWN = node + Node(x=1, y=0, distance=down_weight)
    LEFT = node + Node(x=0, y=-1, distance=left_weight)
    RIGHT = node + Node(x=0, y=1, distance=right_weight)

    FURTHEST_UP = 0
    FURTHEST_DOWN = len(graph) - 1
    FURTHEST_LEFT = 0
    FURTHEST_RIGHT = len(graph[0]) - 1

    # print(f'{ FURTHEST_RIGHT = }, { FURTHEST_LEFT = }, { FURTHEST_UP = }, { FURTHEST_DOWN = }')

    MOVING_UP = node.current_x < 0
    MOVING_DOWN = node.current_x > 0
    MOVING_LEFT = node.current_y < 0
    MOVING_RIGHT = node.current_y > 0

    # start node
    if node.x == FURTHEST_UP and node.y == FURTHEST_LEFT and node.current_x == 0 and node.current_y == 0:
        return [DOWN, RIGHT]
    # corner nodes
    elif node.x == FURTHEST_UP and node.y == FURTHEST_LEFT and node.current_y == 0:
        return [RIGHT]
    elif node.x == FURTHEST_UP and node.y == FURTHEST_LEFT and node.current_x == 0:
        return [DOWN]
    elif node.x == FURTHEST_UP and node.y == FURTHEST_RIGHT and node.current_y == 0:
        return [LEFT]
    elif node.x == FURTHEST_UP and node.y == FURTHEST_RIGHT and node.current_x == 0:
        return [DOWN]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_LEFT and node.current_y == 0:
        return [RIGHT]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_LEFT and node.current_x == 0:
        return [UP]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_RIGHT and node.current_y == 0:
        return [LEFT]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_RIGHT and node.current_x == 0:
        return [UP]

    # side x = 0 nodes
    elif node.x == FURTHEST_UP and node.current_x == 3:
        assert False  # Impossible state
    elif node.x == 0 and node.current_x > 0:
        assert False  # Impossible state
    elif node.x == FURTHEST_UP and node.current_x < 0:
        return [LEFT, RIGHT]
    elif node.x == FURTHEST_UP and node.current_y == 3:
        return [DOWN]
    elif node.x == FURTHEST_UP and node.current_y > 0:
        return [DOWN, RIGHT]
    elif node.x == FURTHEST_UP and node.current_y == -3:
        return [DOWN]
    elif node.x == FURTHEST_UP and node.current_y < 0:
        return [DOWN, LEFT]

    # side x = len(graph) - 1 nodes
    elif node.x == FURTHEST_DOWN and node.current_x > 0:
        return [LEFT, RIGHT]
    elif node.x == FURTHEST_DOWN and node.current_x == -3:
        assert False  # Impossible state
    elif node.x == FURTHEST_DOWN and node.current_x < 0:
        assert False  # Impossible state
    elif node.x == FURTHEST_DOWN and node.current_y == 3:
        return [UP]
    elif node.x == FURTHEST_DOWN and node.current_y > 0:
        return [UP, RIGHT]
    elif node.x == FURTHEST_DOWN and node.current_y == -3:
        return [UP]
    elif node.x == FURTHEST_DOWN and node.current_y < 0:
        return [UP, LEFT]

    # side y = 0 nodes
    elif node.y == FURTHEST_LEFT and node.current_y == 3:
        assert False  # Impossible state
    elif node.y == FURTHEST_LEFT and node.current_y > 0:
        assert False  # Impossible state
    elif node.y == FURTHEST_LEFT and node.current_y < 0:
        return [UP, DOWN]
    elif node.y == FURTHEST_LEFT and node.current_x == 3:
        return [RIGHT]
    elif node.y == FURTHEST_LEFT and node.current_x > 0:
        return [RIGHT, DOWN]
    elif node.y == FURTHEST_LEFT and node.current_x == -3:
        return [RIGHT]
    elif node.y == FURTHEST_LEFT and node.current_x < 0:
        return [RIGHT, UP]

    # side y = len(graph[0]) - 1 nodes
    elif node.y == FURTHEST_RIGHT and node.current_y > 0:
        return [UP, DOWN]
    elif node.y == FURTHEST_RIGHT and node.current_y == -3:
        assert False  # Impossible state
    elif node.y == FURTHEST_RIGHT and node.current_y < 0:
        assert False  # Impossible state
    elif node.y == FURTHEST_RIGHT and node.current_x == 3:
        return [LEFT]
    elif node.y == FURTHEST_RIGHT and node.current_x > 0:
        return [LEFT, DOWN]
    elif node.y == FURTHEST_RIGHT and node.current_x == -3:
        return [LEFT]
    elif node.y == FURTHEST_RIGHT and node.current_x < 0:
        return [LEFT, UP]

    # interior nodes
    elif node.current_x == 3:
        return [LEFT, RIGHT]
    elif node.current_x > 0:
        return [LEFT, RIGHT, DOWN]
    elif node.current_x == -3:
        return [LEFT, RIGHT]
    elif node.current_x < 0:
        return [LEFT, RIGHT, UP]
    elif node.current_y == 3:
        return [UP, DOWN]
    elif node.current_y > 0:
        return [UP, DOWN, RIGHT]
    elif node.current_y == -3:
        return [UP, DOWN]
    elif node.current_y < 0:
        return [UP, DOWN, LEFT]
    else:
        assert False  # Impossible state
    assert False  # Impossible state


def dijkstra(graph, start, end):
    # history = {}
    start_node = Node(x=start[0], y=start[1])
    end_node = Node(x=end[0], y=end[1])
    to_consider = []
    to_consider.append(start_node)

    heapq.heapify(to_consider)

    visited = []
    while len(to_consider) > 0:
        current_node = heapq.heappop(to_consider)
        if current_node.x == end_node.x and current_node.y == end_node.y:
            # print_history(history, current_node, graph)
            return current_node.distance

        in_visited = False
        for node in visited:
            if node == current_node:
                in_visited = True
                break
        if in_visited:
            continue
        visited.append(current_node)
        # print(current_node)
        neighbors = get_neighbors(graph, current_node)
        """
        if Node(distance=57, x=12, y=1, current_x=0, current_y=-1) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()
        if Node(distance=7, x=-1, y=1, current_x=-1, current_y=0) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=9, x=-1, y=2, current_x=0, current_y=1) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=10, x=0, y=2, current_x=1, current_y=0) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=6, x=1, y=-1, current_x=0, current_y=-1) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=10, x=2, y=-1, current_x=1, current_y=0) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(x=2, y=0, current_x=0, current_y=1, distance=13) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()
        """
        # print(current_node, neighbors)
        # print(current_node)
        # input()
        for neighbor in neighbors:
            heapq.heappush(to_consider, neighbor)
            # history[neighbor] = current_node


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[int(elem) for elem in line.strip()] for line in data]

        distance = dijkstra(data, (0, 0), (len(data) - 1, len(data[0]) - 1))
        print(distance)
        assert distance < 1115


if __name__ == '__main__':
    main()
