import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = list(map(int,data))

data.sort()

dat = data + [data[-1]+3]

data = [0] + data

threes = 0
ones = 0

for i, elem in enumerate(data):
    diff = dat[i]-data[i]
    threes += diff == 3
    ones += diff == 1
print(ones)
print(threes)
print(ones * threes)
