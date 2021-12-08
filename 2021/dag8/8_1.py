import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row[:-1] for row in data]
    data = [row.split(' | ') for row in data]
    nums = [elem[0].split(' ') for elem in data]
    output = [elem[1].split(' ') for elem in data]
#print(output)
print(sum([sum([1 for elem in row if len(elem) in [2, 3, 4, 7]]) for row in output]))
