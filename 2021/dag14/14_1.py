import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]

    

rule = {}
template = [elem for elem in data[0]]

elems = []

for elem in data[2:]:
    tup, c = elem.split(' -> ')
    rule[(tup[0], tup[1])] = c
    if tup[0] not in elems:
        elems.append(tup[0])
    if tup[1] not in elems:
        elems.append(tup[1])


def step(template):
    result = []
    for elem in template[:-1]:
        result.append(template[0])
        template = template[1:]
        result.append(rule[(result[-1], template[0])])

    result.append(template[0])
    return result


#print(''.join(template))
niter = 0
while niter < 10:
    template = step(template)
    niter += 1

counts = [template.count(elem) for elem in elems]
counts.sort()
print(counts[-1] - counts[0])

