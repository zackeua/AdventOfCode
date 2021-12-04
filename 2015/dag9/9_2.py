from itertools import permutations

with open('small9.txt', 'r') as f:
    data = f.readlines()

data = [row.split(' = ') for row in data]

data = [(i.split(' to '), j) for i, j in data]

edges = {}
cities = set()
for i, j in data:
    edges[(i[0], i[1])] = int(j)
    edges[(i[1], i[0])] = int(j)

    if i[0] not in cities:
            cities.add(i[0])
    if i[1] not in cities:
            cities.add(i[1])

print(cities)
print(edges)

maxLen = float('-Inf')

for comb in permutations(cities, len(cities)):
    valid = True
    tempLen = 0
    for i1,i2 in zip(comb[:-1], comb[1:]):
        if (i1, i2) in edges and valid:
            tempLen += edges[(i1, i2)]
        else:
            valid = False
    if valid:
        print(f'{comb}: {tempLen}')
        if maxLen < tempLen:
            maxLen = tempLen
print(maxLen)
