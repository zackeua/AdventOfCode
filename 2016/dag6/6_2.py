import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.strip() for row in data]
    print(data)

words = [[] for _ in range(len(data[0]))]

for i, _ in enumerate(data[0]):
    for j, _ in enumerate(data):
        words[i].append(data[j][i])

counts = [[(letter, row.count(letter)) for letter in 'abcdefghijklmnopqrtsuvwxyz'] for row in words]

counts = [sorted(row, key=lambda x:x[1], reverse=True) for row in counts]
counts = [[elem for elem in row if elem[1] != 0] for row in counts]


result = ''.join([counts[i][-1][0] for i in range(len(data[0]))])

print(result)