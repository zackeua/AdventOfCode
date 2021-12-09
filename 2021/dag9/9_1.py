import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [[int(elem) for elem in row if elem != '\n'] for row in data]

totsum = 0

for i, row in enumerate(data):
    for j, elem in enumerate(row):
        minimum = True
        if i != 0 and elem >= data[i-1][j]: minimum = False

        if j != 0 and elem >= data[i][j-1]: minimum = False

        if i != len(data)-1 and elem >= data[i+1][j]: minimum = False

        if j != len(data[0]) - 1 and elem >= data[i][j+1]: minimum = False

        if minimum:
            totsum += data[i][j] + 1
print(totsum)