import sys
import networkx as nx
with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [[int(elem) for elem in row] for row in data]

G = nx.DiGraph()
bigger_data = []
for i_index in range(5):
    for i, row in enumerate(data):
        temp_row = []
        for j_index in range(5):
            for j, val in enumerate(row):
                x_index = i+i_index*len(data)
                y_index = j+j_index*len(data[0])
                weight = data[(i)%(len(data))][(j)%(len(data[0]))] + i_index + j_index
                if weight > 9:
                    weight -= 9
                #print(weight, end = '')
                temp_row.append(weight)
        bigger_data.append(temp_row)
        #print()

for i, row in enumerate(bigger_data):
    for j, val in enumerate(row):
        if i < len(bigger_data)-1:
            G.add_edge((i, j), (i+1, j), weight = bigger_data[i+1][j])
        if i > 0:
            G.add_edge((i, j), (i-1, j), weight = bigger_data[i-1][j])
        if j < len(bigger_data[0])-1:
            G.add_edge((i, j), (i, j+1), weight = bigger_data[i][j+1])
        if j > 0:
            G.add_edge((i, j), (i, j-1), weight = bigger_data[i][j-1])


dist, path = nx.single_source_dijkstra(G, (0,0))

endnode = (len(bigger_data)-1, len(bigger_data[0])-1)
print(dist[endnode])
