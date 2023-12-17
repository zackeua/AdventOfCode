import sys
import dataclasses


@dataclasses.dataclass
class Node:
    distance: int = 0
    x: int = 0
    y: int = 0
    current_x: int = 0
    current_y: int = 0


def get_neighbors(graph, node):
    if node.x == 0:
        if node.y == 0:
            if node.current_x == 0 and node.current_y == 0:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y]),
                             Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
            elif node.current_x != 0:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
            elif node.current_y != 0:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y])]

        elif node.y == len(graph[0]) - 1:
            if node.current_x != 0:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
            elif node.current_y != 0:
                neighbors = [Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]

        else:
            if node.current_x > 0:
                if node.current_x == 3:
                    neighbors = [Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
                else:
                    neighbors = [Node(x=node.x + 1, y=node.y, current_x=node.current_x + 1, current_y=node.current_y, distance=node.distance + graph[node.x + 1][node.y]),
                                 Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
            elif node.current_x < 0:
                if node.current_x == -3:
                    neighbors = [Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
                else:
                    neighbors = [Node(x=node.x - 1, y=node.y, current_x=node.current_x - 1, current_y=node.current_y, distance=node.distance + graph[node.x - 1][node.y]),
                                 Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
            else:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y]),
                             Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
    elif node.x == len(graph) - 1:
        if node.y == 0:
            if node.current_x != 0:
                neighbors = [Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
            elif node.current_y != 0:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1])]
        elif node.y == len(graph[0]) - 1:
            if node.current_x != 0:
                neighbors = [Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
            elif node.current_y != 0:
                neighbors = [Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
        else:
            if node.current_x > 0:
                if node.current_x == 3:
                    neighbors = [Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
                else:
                    neighbors = [Node(x=node.x + 1, y=node.y, current_x=node.current_x + 1, current_y=node.current_y, distance=node.distance + graph[node.x + 1][node.y]),
                                 Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
            elif node.current_x < 0:
                if node.current_x == -3:
                    neighbors = [Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
                else:
                    neighbors = [Node(x=node.x - 1, y=node.y, current_x=node.current_x - 1, current_y=node.current_y, distance=node.distance + graph[node.x - 1][node.y]),
                                 Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
    elif node.y == 0:
        if node.current_y > 0:
            if node.current_y == 3:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y])]
            else:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=node.current_x, current_y=node.current_y + 1, distance=node.distance + graph[node.x][node.y + 1]),
                             Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y])]
        elif node.current_y < 0:
            if node.current_y == -3:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y])]
            else:
                neighbors = [Node(x=node.x, y=node.y - 1, current_x=node.current_x, current_y=node.current_y - 1, distance=node.distance + graph[node.x][node.y - 1]),
                             Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y])]
        else:
            neighbors = [Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y]),
                         Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y])]
    elif node.y == len(graph[0]) - 1:
        if node.current_y > 0:
            if node.current_y == 3:
                neighbors = [Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
            else:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=node.current_x, current_y=node.current_y + 1, distance=node.distance + graph[node.x][node.y + 1]),
                             Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
        elif node.current_y < 0:
            if node.current_y == -3:
                neighbors = [Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
            else:
                neighbors = [Node(x=node.x, y=node.y - 1, current_x=node.current_x, current_y=node.current_y - 1, distance=node.distance + graph[node.x][node.y - 1]),
                             Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
        else:
            neighbors = [Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y]),
                         Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y])]
    else:
        if node.current_x > 0:
            if node.current_x == 3:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1]),
                             Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
            else:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=node.current_x + 1, current_y=node.current_y, distance=node.distance + graph[node.x + 1][node.y]),
                             Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1]),
                             Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
        elif node.current_x < 0:
            if node.current_x == -3:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1]),
                             Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
            else:
                neighbors = [Node(x=node.x - 1, y=node.y, current_x=node.current_x - 1, current_y=node.current_y, distance=node.distance + graph[node.x - 1][node.y]),
                             Node(x=node.x, y=node.y + 1, current_x=0, current_y=1, distance=node.distance + graph[node.x][node.y + 1]),
                             Node(x=node.x, y=node.y - 1, current_x=0, current_y=-1, distance=node.distance + graph[node.x][node.y - 1])]
        elif node.current_y > 0:
            if node.current_y == 3:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y]),
                             Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
            else:
                neighbors = [Node(x=node.x, y=node.y + 1, current_x=node.current_x, current_y=node.current_y + 1, distance=node.distance + graph[node.x][node.y + 1]),
                             Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y]),
                             Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
        elif node.current_y < 0:
            if node.current_y == -3:
                neighbors = [Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y]),
                             Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]
            else:
                neighbors = [Node(x=node.x, y=node.y - 1, current_x=node.current_x, current_y=node.current_y - 1, distance=node.distance + graph[node.x][node.y - 1]),
                             Node(x=node.x + 1, y=node.y, current_x=1, current_y=0, distance=node.distance + graph[node.x + 1][node.y]),
                             Node(x=node.x - 1, y=node.y, current_x=-1, current_y=0, distance=node.distance + graph[node.x - 1][node.y])]

    # print(node, neighbors)
    # input()
    return neighbors


def dijkstra(graph, start, end):
    start_node = Node(x=start[0], y=start[1])
    end_node = Node(x=end[0], y=end[1])
    to_consider = []
    to_consider.append(start_node)
    visited = []
    while to_consider != []:
        current_node = to_consider.pop(0)
        if current_node.x == end_node.x and current_node.y == end_node.y:
            return current_node.distance
        for node in visited:
            if node.x == current_node.x and node.y == current_node.y and node.current_x == current_node.current_x and node.current_y == current_node.current_y:
                continue

        visited.append(current_node)
        for neighbor in get_neighbors(graph, current_node):
            to_consider.append(neighbor)


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[int(elem) for elem in line.strip()] for line in data]
        
        distance = dijkstra(data, (0, 0), (len(data) - 1, len(data[0]) - 1))
        print(distance)

if __name__ == '__main__':
    main()
