import sys
d = {}
def rec(li):
    if sum([item+1 for item in li]) not in d:
        tot = 0
        if len(li)>= 3:
            if li[2] - li[0] <= 3:
                tot += 1
                tot += rec([li[0]] + li[2:])
            tot += rec(li[1:])
        d[sum([item+1 for item in li])] = tot
    return d[sum([item+1 for item in li])]


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = list(map(int,data))

data.sort()
data = [0] + data + [data[-1]+3]
print(rec(data)+1)
print(data)
#print()
#print(check(data))
