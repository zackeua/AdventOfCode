import sys
with open(sys.argv[1], 'r') as f:
    data = list(map(int,f.readlines()))

d = {}
for item in data:
    if 2020-item not in d:
        d[item] = item
    else:
        print(f'{(2020-item)*item}')
