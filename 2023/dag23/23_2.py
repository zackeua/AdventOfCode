import sys
from copy import deepcopy


def get_neighbors(graph, node, visited):
    neighbors = []

    #print(graph[node[0]][node[1]], node[0] , node[1], visited)
    # input()
    if graph[node[0] - 1][node[1]] not in '#' and (node[0] - 1, node[1]) not in visited:
        neighbors.append((node[0] - 1, node[1]))

    if graph[node[0] + 1][node[1]] not in '#' and (node[0] + 1, node[1]) not in visited:
        neighbors.append((node[0] + 1, node[1]))

    if graph[node[0]][node[1] - 1] not in '#' and (node[0], node[1] - 1) not in visited:
        neighbors.append((node[0], node[1] - 1))

    if graph[node[0]][node[1] + 1] not in '#' and (node[0], node[1] + 1) not in visited:
        neighbors.append((node[0], node[1] + 1))

    return neighbors


def dfs(graph, start, end, visited):
    distance = 0
    local_visited = deepcopy(visited)
    neighbor = start
    local_visited.add(start)
    while neighbor != end:
        neighbors = get_neighbors(graph, neighbor, local_visited)
        if len(neighbors) == 0:
            # print('no neighbors', neighbor, end)
            return 0, local_visited
        elif len(neighbors) == 1 and neighbors[0] == end:
            local_visited.add(neighbors[0])
            return len(local_visited), local_visited
        elif len(neighbors) == 1:
            local_visited.add(neighbors[0])
            neighbor = neighbors[0]
        else:
            best_distance = 0
            local_result = deepcopy(local_visited)
            for neighbor in neighbors:
                tmp_visited = deepcopy(local_visited)
                tmp_visited.add(neighbor)
                tmp_dist, tmp_visited = dfs(graph, neighbor, end, tmp_visited)
                # show_history(graph, tmp_visited, start, end)
                # print(tmp_dist, neighbor, neighbors, distance)
                # input()
                if tmp_dist > best_distance:
                    best_distance = tmp_dist
                    local_result = deepcopy(tmp_visited)

            if len(local_result) > len(local_visited):
                local_visited = deepcopy(local_result)
            return len(local_result), local_visited

    return len(local_visited), local_visited


def show_history(graph, history, start, end):

    for i, line in enumerate(graph):
        for j, char in enumerate(line):
            if (i, j) in history:
                print('X', end='')
            else:
                print(char, end='')
        print()
    print()


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        start_x = data[0].find('.')
        end_x = data[-1].find('.')
        visited = set()
        visited.add((0, start_x))
        start = (1, start_x)
        end = (len(data) - 1, end_x)
        for line in data:
            print(line)
        print(start, end)
        result, visited = dfs(data, start, end, visited)
        show_history(data, visited, start, end)
        result -= 1
        print(result)

        assert result > 1798


if __name__ == '__main__':
    main()
