import sys
import heapq


def get_neighbors(graph, node, visited):
    neighbors = []

    if node[0] != 0:

        if graph[node[0] - 1][node[1]] in '.^' and (node[0] - 1, node[1]) not in visited:
            local_visited = visited
            if graph[node[0] - 1][node[1]] == '^':
                local_visited = visited.copy()
            neighbors.append(((node[0] - 1, node[1]), local_visited))

        if graph[node[0] + 1][node[1]] in '.v' and (node[0] + 1, node[1]) not in visited:
            local_visited = visited
            if graph[node[0] + 1][node[1]] == 'v':
                local_visited = visited.copy()
            neighbors.append(((node[0] + 1, node[1]), local_visited))

        if graph[node[0]][node[1] - 1] in '.<' and (node[0], node[1] - 1) not in visited:
            local_visited = visited
            if graph[node[0]][node[1] - 1] == '<':
                local_visited = visited.copy()
            neighbors.append(((node[0], node[1] - 1), local_visited))

        if graph[node[0]][node[1] + 1] in '.>' and (node[0], node[1] + 1) not in visited:
            local_visited = visited
            if graph[node[0]][node[1] + 1] == '>':
                local_visited = visited.copy()
            neighbors.append(((node[0], node[1] + 1), local_visited))
    else:
        neighbors.append((node[0] + 1, node[1], visited))

    return neighbors


def dijkstra(graph, start, end):
    history = {}
    to_visit = []
    visited = set()
    heapq.heappush(to_visit, (0, ((start[0], start[1]), visited)))
    while to_visit != []:
        cost, node = heapq.heappop(to_visit)

        if node in visited:
            continue
        print(node)
        if node[:2] == end:
            return -cost, history
        visited.add(node)
        neighbors = get_neighbors(graph, node[0], node[1])
        print(node, neighbors)
        for neighbor in neighbors:
            if neighbor not in visited:
                history[(neighbor[0], neighbor[1])] = (node[0], node[1])
                heapq.heappush(to_visit, (cost - 1, neighbor))


def show_history(graph, history, start, end):

    current = end
    while current != start[:2]:
        graph[current[0]][current[1]] = 'O'
        current = history[current]
    graph[current[0]][current[1]] = 'O'
    for line in graph:
        print(line)


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        start_x = data[0].find('.')
        end_x = data[-1].find('.')
        start = (0, start_x, -1, start_x)
        end = (len(data) - 1, end_x)
        for line in data:
            print(line)
        print(start, end)
        result, history = dijkstra(data, start, end)
        print(result)

        assert result > 1798


if __name__ == '__main__':
    main()
