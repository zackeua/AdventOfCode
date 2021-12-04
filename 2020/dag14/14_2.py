import re
import sys
def app(num,list):
    l = []
    for item in list:
        l.append(item + num)
    return l

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
    s = ['']
    for i, elem in enumerate(bitmask):
        if elem == 'X':
            s = app('1',s) + app('0',s)
        elif elem == '0':
            s = app(bitnum[i],s)
        else:
            s = app('1',s)
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
        val = int(p[1])
        locations = mask(num2bit(int(p[0])),bitmask)
        for loc in locations:
            d[bit2num(loc)] = val


tot = 0

for key in list(d.keys()):
    tot += d[key]

print(tot)
