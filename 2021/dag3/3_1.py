import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()

ones = [0]*len(data[0][:-1])
zeros = [0]*len(data[0][:-1])

for i, row in enumerate(data):
    #print(row)
    for j, elem in enumerate(row[:-1]):
        if int(elem):
            ones[j] += 1
        else:
            zeros[j] += 1

gamma = int(''.join([str(int(i > j)) for i, j in zip(ones, zeros)]),2)
epsilon = int(''.join([str(int(i < j)) for i, j in zip(ones, zeros)]),2)

print(gamma)
print(epsilon)
print(gamma * epsilon)
