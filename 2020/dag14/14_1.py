import re
import sys
def num2bit(num):
    s = ''
    for _ in range(36):
        if num%2==0:
            s = '0' + s
        else:
            s = '1' + s
        num = num//2
    return s

def mask(bitnum,bitmask):
    s = ''
    for i, elem in enumerate(bitmask):
        if elem == 'X':
            s = s + bitnum[i]
        else:
            s = s + elem
    return s

def bit2num(bitnum):
    num = 0
    for bit in bitnum:
        num = num * 2
        if bit == '1':
            num = num + 1
    return num

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
d = {}

for line in data:
    line = line[:-1]
    if 'mask' in line:
        bitmask = line[7:]
        print(bitmask)
    else:
        line = re.sub("mem\[","",line)
        line = re.sub("]","",line)
        p = line.split('=')
        d[int(p[0])] = bit2num(mask(num2bit(int(p[1])),bitmask))


tot = 0

for key in list(d.keys()):
    tot += d[key]

print(tot)
