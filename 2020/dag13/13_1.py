import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    travelTime = int(data[0])
    lines = data[1].split(',')
    lines = [line for line in lines if 'x' not in line]
    lines = list(map(int,lines))
print(travelTime)
print(lines)


minDiff = travelTime

for line in lines:
    times = 1
    while times*line < travelTime:
        times += 1
    if times*line - travelTime < minDiff:
        minDiff = times*line-travelTime
        minID = line

print(minID*minDiff)
