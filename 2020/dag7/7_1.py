import sys
import re
with open(sys.argv[1], 'r') as f:
    data = f.read()
    #print(data)
    data = re.sub("\n","",data)
    data = re.sub(" [0-9] ", "", data)
    data = re.sub(" bags", "" , data)
    data = re.sub(" bag", "" ,data)
    data = re.sub(" contain", ",",data)
    #print(data)
    data = data.split('.')[:-1]
    #print(data)


d = {}

for row in data:
    items = row.split(',')
    #print(items)
    if items[1] != " no other":
        for i in items[1:]:
            if i not in d:
                d[i] = []
            d[i].append(items[0])

l = d["shiny gold"]
visited = []

while l:
    visited.append(l[0])
    if l[0] in d:
        for elem in d[l[0]]:
            if elem not in visited and elem not in l:
                l.append(elem)
    l.pop(0)


print(len(visited))
