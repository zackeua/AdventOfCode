import sys
import networkx as nx

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.replace('\n', '') for line in data]
    
        graph = nx.DiGraph()
        for i, line in enumerate(data):
            for j, elem in enumerate(line):
                if elem == 'S':
                    start_node = (i, j)
                if elem == 'E':
                    end_node = (i, j)
                search_dirs = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]
                for search_dir in search_dirs:
                    a, b = search_dir
                    if 0 <= a < len(data) and 0 <= b < len(data[0]):
                        if ord(elem) + 2 > ord(data[a][b]) and data[a][b] not in ['S', 'E'] or elem == 'S' and data[a][b] in ['b', 'a'] or elem in ['y', 'z'] and data[a][b] == 'E':
                            graph.add_edge((i, j), search_dir, weight=1)
                                

        
        dist, _ = nx.single_source_dijkstra(graph, start_node)
        
        print(dist[end_node])
    

if __name__ == '__main__':
    main()