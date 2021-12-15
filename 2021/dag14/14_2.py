import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]

    

rule = {}

template = {}
for i in range(len(data[0])-1):
    if (data[0][i], data[0][i+1]) not in template:
        template[(data[0][i], data[0][i+1])] = 1
    else:
        template[(data[0][i], data[0][i+1])] += 1

#template = [elem for elem in data[0]] # store tuple as key and count as val in hash map

elems = []


for elem in data[2:]:
    tup, c = elem.split(' -> ')
    rule[(tup[0], tup[1])] = c
    if tup[0] not in elems:
        elems.append(tup[0])
    if tup[1] not in elems:
        elems.append(tup[1])

counts = {elem:0 for elem in elems}

for C in data[0]:
    counts[C] += 1

def step(template):
    result = {}
    for elem in template:
        C = rule[elem]
        counts[C] += template[elem]
        if (elem[0], C) not in result:
            result[(elem[0], C)] = template[elem]
        else:
            result[(elem[0], C)] += template[elem]
        
        if (C, elem[1]) not in result:
            result[(C, elem[1])] = template[elem]
        else:
            result[(C, elem[1])] += template[elem]
    return result


niter = 0
while niter < 40:
    template = step(template)
    niter += 1

counts = [counts[key] for key in counts]
'''
counts = [0 for _ in elems]

for item in template:
    for i, c in enumerate(elems):
        if c == item[0]:
            counts[i] += template[item]
        if c == item[1]:
            counts[i] += template[item]
'''



#counts = [count for count in counts]
#print(template)
#print(elems)
#print(counts)
counts.sort()
print((counts[-1] - counts[0]))
#print(template)
#NCNBCHB
