import sys
import networkx as nx


def visualise(path, blocked_spaces):
    for j in range(0, 7):
        for i in range(0, 7):
            if (i, j) in blocked_spaces:
                print('#', end='')
            elif (i, j) in path:
                print('O', end='')
            else:
                print('.', end='')
        print()


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [tuple(map(int, line.strip().split(','))) for line in data]
        # print(data)

    for blocks in range(1024, len(data)):
        blocked_spaces = data[:blocks+1]
        for i in range(0, 70):
            blocked_spaces.append((-1, i))
            blocked_spaces.append((71, i))
            blocked_spaces.append((i, -1))
            blocked_spaces.append((i, 71))

        blocked_spaces = set(blocked_spaces)
        graph = nx.DiGraph()
        for i in range(0, 71):
            for j in range(0, 71):
                if (i, j) in blocked_spaces:
                    continue

                if (i - 1, j) not in blocked_spaces:
                    graph.add_edge((i, j), (i-1, j))
                    # graph.add_edge((i-1, j), (i, j))
                if (i + 1, j) not in blocked_spaces:
                    graph.add_edge((i, j), (i+1, j))
                    # graph.add_edge((i+1, j), (i, j))
                if (i, j - 1) not in blocked_spaces:
                    graph.add_edge((i, j), (i, j-1))
                    # graph.add_edge((i, j-1), (i, j))
                if (i, j + 1) not in blocked_spaces:
                    graph.add_edge((i, j), (i, j+1))
                    # graph.add_edge((i, j+1), (i, j))
        try:
            _ = nx.shortest_path_length(graph, (0, 0), (70, 70))
        except:
            print(f'{data[blocks][0]},{data[blocks][1]}')
            sys.exit()


if __name__ == '__main__':
    main()
