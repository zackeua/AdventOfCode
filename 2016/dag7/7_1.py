import sys
import re

with open(sys.argv[1], 'r') as f:
    data = [row.strip() for row in f.readlines()]


count = 0
for row in data:
    result1 = False
    result2 = True
    flag = False
    for i1, i2, i3, i4 in zip(row[:-3],row[1:-2],row[2:-1],row[3:]):

        if '[' not in [i1, i2, i3, i4] and ']' not in [i1, i2, i3, i4]:
            if [i1, i2] == [i4, i3] and i1 != i2 and not flag: result1 = True
            if [i1, i2] == [i4, i3] and i1 != i2 and flag: result2 = False
        elif '[' == i1:
            flag = True
        elif ']' == i1:
            flag = False
        #print(''.join([i1, i2, i3, i4]), result1 and result2)
    result = result1 and result2

    #print(row, result)

    count += result


print(count)