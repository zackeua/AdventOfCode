import sys
import dataclasses
import heapq
import networkx as nx

@dataclasses.dataclass
class Node:
    distance: int = 0
    x: int = 0
    y: int = 0
    x_direction: int = 0
    y_direction: int = 0
    current_moves: int = 0

    def __init__(self, x=0, y=0, x_direction=0, y_direction=0, current_moves=0, distance=0):
        self.x = x
        self.y = y
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.current_moves = current_moves
        self.distance = distance

    def __add__(self, other):
        next_x = self.x + other.x_direction
        next_y = self.y + other.y_direction
        
        current_moves = self.current_moves + 1
        
        if next_x < self.x:
            d_x = -1
        elif next_x > self.x:
            d_x = 1
        elif next_x == self.x:
            d_x = 0

        if next_y < self.y:
            d_y = -1
        elif next_y > self.y:
            d_y = 1
        elif next_y == self.y:
            d_y = 0
        if other.x_direction != self.x_direction:
            current_moves = 1

        return Node(x=next_x,
                    y=next_y,
                    x_direction=other.x_direction,
                    y_direction=other.y_direction,
                    current_moves=current_moves,
                    distance=self.distance + other.distance)

    def __lt__(self, other):
        return (self.distance, - self.x - self.y) < (other.distance, - other.x - other.y)

    def __eq__(self, other):
        return (self.x, self.y, self.x_direction, self.y_direction, self.current_moves, self.distance) == \
               (other.x, other.y, other.x_direction, other.y_direction, other.current_moves, other.distance)

    def __hash__(self):
        return hash((self.x, self.y, self.x_direction, self.y_direction))

    def copy(self):
        return Node(x=self.x,
                    y=self.y,
                    x_direction=self.x_direction,
                    y_direction=self.y_direction,
                    current_moves=self.current_moves,
                    distance=self.distance)

def print_history(history, node, graph):

    nodes = []
    nodes.append(node)
    tmp_node = node.copy()
    while tmp_node in history:
        tmp_node = history[tmp_node]
        nodes.append(tmp_node.copy())

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

def print_history_2(path, graph):
    for x, row in enumerate(graph):
        for y, elem in enumerate(row):
            printed = False
            for node in path:
                if type(node) == tuple and  node[0] == x and node[1] == y:
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

    UP = node + Node(x_direction=-1, y_direction=0, distance=up_weight)
    DOWN = node + Node(x_direction=1, y_direction=0, distance=down_weight)
    LEFT = node + Node(x_direction=0, y_direction=-1, distance=left_weight)
    RIGHT = node + Node(x_direction=0, y_direction=1, distance=right_weight)

    FURTHEST_UP = 0
    FURTHEST_DOWN = len(graph) - 1
    FURTHEST_LEFT = 0
    FURTHEST_RIGHT = len(graph[0]) - 1

    # print(f'{ FURTHEST_RIGHT = }, { FURTHEST_LEFT = }, { FURTHEST_UP = }, { FURTHEST_DOWN = }')

    MOVING_UP = node.x_direction < 0
    MOVING_DOWN = node.x_direction > 0
    MOVING_LEFT = node.y_direction < 0
    MOVING_RIGHT = node.y_direction > 0

    # start node
    if node.x == FURTHEST_UP and node.y == FURTHEST_LEFT and node.x_direction == 0 and node.y_direction == 0:
        return [DOWN, RIGHT]
    # corner nodes
    elif node.x == FURTHEST_UP and node.y == FURTHEST_LEFT and node.y_direction == 0:
        return [RIGHT]
    elif node.x == FURTHEST_UP and node.y == FURTHEST_LEFT and node.x_direction == 0:
        return [DOWN]
    elif node.x == FURTHEST_UP and node.y == FURTHEST_RIGHT and node.y_direction == 0:
        return [LEFT]
    elif node.x == FURTHEST_UP and node.y == FURTHEST_RIGHT and node.x_direction == 0:
        return [DOWN]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_LEFT and node.y_direction == 0:
        return [RIGHT]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_LEFT and node.x_direction == 0:
        return [UP]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_RIGHT and node.y_direction == 0:
        return [LEFT]
    elif node.x == FURTHEST_DOWN and node.y == FURTHEST_RIGHT and node.x_direction == 0:
        return [UP]

    # side x = 0 nodes
    elif node.x == FURTHEST_UP and node.x_direction > 0:
        assert False  # Impossible state
    elif node.x == FURTHEST_UP and node.x_direction < 0:
        return [LEFT, RIGHT]
    elif node.x == FURTHEST_UP and node.y_direction > 0:
        if node.current_moves == 3:
            return [DOWN]
        return [RIGHT, DOWN]
    elif node.x == FURTHEST_UP and node.y_direction < 0:
        if node.current_moves == 3:
            return [DOWN]
        return [DOWN, LEFT]

    # side x = len(graph) - 1 nodes
    elif node.x == FURTHEST_DOWN and node.x_direction > 0:
        return [LEFT, RIGHT]
    elif node.x == FURTHEST_DOWN and node.x_direction < 0:
        assert False  # Impossible state
    elif node.x == FURTHEST_DOWN and node.y_direction > 0:
        if node.current_moves == 3:
            return [UP]
        return [RIGHT, UP]
    elif node.x == FURTHEST_DOWN and node.y_direction < 0:
        if node.current_moves == 3:
            return [UP]
        return [UP, LEFT]

    # side y = 0 nodes
    elif node.y == FURTHEST_LEFT and node.y_direction > 0:
        assert False  # Impossible state
    elif node.y == FURTHEST_LEFT and node.y_direction < 0:
        return [UP, DOWN]
    elif node.y == FURTHEST_LEFT and node.x_direction > 0:
        if node.current_moves == 3:
            return [RIGHT]
        return [RIGHT, DOWN]
    elif node.y == FURTHEST_LEFT and node.x_direction < 0:
        if node.current_moves == 3:
            return [RIGHT]
        return [RIGHT, UP]

    # side y = len(graph[0]) - 1 nodes
    elif node.y == FURTHEST_RIGHT and node.y_direction > 0:
        return [UP, DOWN]
    elif node.y == FURTHEST_RIGHT and node.y_direction < 0:
        assert False  # Impossible state
    elif node.y == FURTHEST_RIGHT and node.x_direction > 0:
        if node.current_moves == 3:
            return [LEFT]
        return [LEFT, DOWN]
    elif node.y == FURTHEST_RIGHT and node.x_direction < 0:
        if node.current_moves == 3:
            return [LEFT]
        return [LEFT, UP]

    # interior nodes
    elif node.x_direction > 0:
        if node.current_moves == 3:
            return [LEFT, RIGHT]
        return [LEFT, RIGHT, DOWN]
    elif node.x_direction < 0:
        if node.current_moves == 3:
            return [LEFT, RIGHT]
        return [LEFT, RIGHT, UP]
    elif node.y_direction > 0:
        if node.current_moves == 3:
            return [UP, DOWN]
        return [UP, DOWN, RIGHT]
    elif node.y_direction < 0:
        if node.current_moves == 3:
            return [UP, DOWN]
        return [UP, DOWN, LEFT]
    else:
        assert False  # Impossible state
    assert False  # Impossible state


def dijkstra(graph, start, end):
    history = {}
    start_node = Node(x=start[0], y=start[1])
    end_node = Node(x=end[0], y=end[1])
    to_consider = []
    to_consider.append(start_node)

    heapq.heapify(to_consider)

    visited = []
    count = 0
    while len(to_consider) > 0:
        current_node = heapq.heappop(to_consider)
        if current_node.x == end_node.x and current_node.y == end_node.y:
            print_history(history, current_node, graph)
            return current_node.distance

        # in_visited = False
        # for node in visited:
        #     if node == current_node:
        #         in_visited = True
        #         break
        # if in_visited:
        #     continue
        visited.append(current_node)
        # print(current_node)
        neighbors = get_neighbors(graph, current_node)
        """
        if Node(distance=57, x=12, y=1, x_direction=0, y_direction=-1) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()
        if Node(distance=7, x=-1, y=1, x_direction=-1, y_direction=0) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=9, x=-1, y=2, x_direction=0, y_direction=1) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=10, x=0, y=2, x_direction=1, y_direction=0) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=6, x=1, y=-1, x_direction=0, y_direction=-1) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(distance=10, x=2, y=-1, x_direction=1, y_direction=0) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()

        if Node(x=2, y=0, x_direction=0, y_direction=1, distance=13) in neighbors:
            print('Found it!')
            print(current_node, neighbors)
            input()
        """
        # print(current_node, neighbors)
        # print(current_node)
        # input()
        for neighbor in neighbors:
            in_visited = False
            for node in visited:
                if node == neighbor:
                    in_visited = True
                    break
            if in_visited:
                continue
            heapq.heappush(to_consider, neighbor)
            if neighbor not in history:
                history[neighbor] = current_node

def sign(x):
    return (x > 0) - (x < 0)

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[int(elem) for elem in line.strip()] for line in data]

        g = nx.DiGraph()
        for x, row in enumerate(data):
            for y, elem in enumerate(row):
                for x_dir, y_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    for steps in range(0, 3):
                        if steps == 2:
                            if x_dir != 0:
                                g.add_edge((x, y, x_dir, y_dir, steps), (x, y + 1, 0, 1, 1), weight=elem)
                                g.add_edge((x, y, x_dir, y_dir, steps), (x, y - 1, 0, -1, 1), weight=elem)
                            elif y_dir != 0:
                                g.add_edge((x, y, x_dir, y_dir, steps), (x + 1, y, 1, 0, 1), weight=elem)
                                g.add_edge((x, y, x_dir, y_dir, steps), (x - 1, y, -1, 0, 1), weight=elem)
                        else:
                            g.add_edge((x, y, x_dir, y_dir, steps), (x + x_dir, y + y_dir, x_dir, y_dir, steps + 1), weight=elem)
   
        for x_dir, y_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for steps in range(0, 4):
                g.add_edge((len(data)-1, len(data[0]) - 1, x_dir, y_dir, steps), (1), weight=0)
                g.add_edge((0), (0, 0, x_dir, y_dir, steps), weight=0)


        distance = nx.dijkstra_path(g, (0), (1))


        print_history_2(distance, data) 

        print(distance)
        assert distance < 1115


if __name__ == '__main__':
    main()
