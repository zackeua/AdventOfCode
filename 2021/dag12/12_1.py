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
    return visited

def search(g, node, visited, count):
    visited_copy = visited.copy()
    visited_copy[node] += 1
    goto = [elem for elem in g[node] if elem.upper() != elem and visited_copy[elem] == 0 or elem.upper() == elem]    
    for elem in goto:
        if elem != 'end':
            count = search(g, elem, visited_copy, count)
        else:
            count += 1
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
count = search(g, node, visited, 0)


print(count)