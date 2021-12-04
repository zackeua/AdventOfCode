import sys

with open(sys.argv[1], 'r') as f:
    data = list(map(int, f.readlines()))

prev = sum(data[:3])
res = 0
for i, val in enumerate(data[:]):
        current = sum(data[i:i+3])
        res += current > prev
        prev = current
        
print(res)
