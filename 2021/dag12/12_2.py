import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]

def add_to_graph(g, key, elem):
    if key in g:
        g[key].append(elem)
    else:
        g[key] = [elem]
    return g

def create_visited(g):
    visited = {}
    for key in g.keys():
        visited[key] = 0
    visited['double'] = None
    return visited

def search(g, node, visited, count): #, path):
    visited_copy = visited.copy()
    visited_copy[node] += 1
    if visited_copy['double'] == None and node.upper() != node and visited_copy[node] == 2:
        visited_copy['double'] = node
    
    #if path != '':
    #    path_copy = path + ',' + node
    #else:
    #    path_copy = '' + node
    
    goto = [elem for elem in g[node] \
        if elem.upper() != elem and visited_copy[elem] < 2 and elem != 'start' and None == visited_copy['double'] \
        or elem.upper() != elem and visited_copy[elem] < 1 and elem != 'start' and elem != visited_copy['double'] \
        or elem.upper() == elem]
    for elem in goto:
        if elem != 'end':
            count = search(g, elem, visited_copy, count) #, path_copy)
        else:
            count += 1
            #print(path_copy + ',' + 'end')
    return count


g = {}
for row in data:
    a, b = row.split('-')
    g = add_to_graph(g, a, b)
    g = add_to_graph(g, b, a)
    #print(row)

#print(g)


visited = create_visited(g)
node = 'start'
path = ''
count = search(g, node, visited, 0) #, path)


print(count)