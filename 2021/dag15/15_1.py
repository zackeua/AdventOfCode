import sys
import networkx as nx
with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [[int(elem) for elem in row] for row in data]

G = nx.DiGraph()

for i, row in enumerate(data):
    for j, val in enumerate(row):
        if i < len(data)-1:
            G.add_edge((i,j), (i+1,j), weight=data[i+1][j])
        if i > 0:
            G.add_edge((i,j), (i-1,j), weight=data[i-1][j])
        if j < len(data[0])-1:
            G.add_edge((i,j), (i,j+1), weight=data[i][j+1])
        if j > 0:
            G.add_edge((i,j), (i,j-1), weight=data[i][j-1])

dist, path = nx.single_source_dijkstra(G, (0,0))

endnode = (len(data)-1, len(data[0])-1)
print(dist[endnode])
