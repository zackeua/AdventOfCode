import sys

from itertools import permutations

persons = []

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.strip()[:-1].split() for row in data]
    for row in data:
        if row[0] not in persons: persons.append(row[0])
    data = {(row[0], row[-1]): (-1 if row[2] == 'lose' else 1) * int(row[3]) for row in data}
    print(data)

    max_score = None
    for perm in permutations(persons):
        score = 0
        score += data[perm[0], perm[-1]]
        score += data[perm[-1], perm[0]]
        for e1, e2 in zip(perm[:-1], perm[1:]):
            score += data[(e1, e2)]
            score += data[(e2, e1)]
        if max_score == None or max_score < score: max_score = score

print(max_score)