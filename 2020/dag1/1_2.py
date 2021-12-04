import sys
with open(sys.argv[1], 'r') as f:
    data = list(map(int,f.readlines()))


d = {}
run = True
for it in data:
    if run:
        for item in [i for i in data if i != it]:
            if 2020-it-item not in d:
                d[item] = item
            else:
                print(f'{it*(2020-it-item)*item}')
                run = False
                break
