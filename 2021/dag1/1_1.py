import sys

with open(sys.argv[1], 'r') as f:
        data = list(map(int,f.readlines()))

res = sum([a < b for a,b in zip(data[:-1], data[1:])])
print(res)