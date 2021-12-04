import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()

ones = 0
zeros = 0

iter = 0
cols = len(data[0][:-1])

ox = data.copy()
o2 = data.copy()
while iter < cols:
    ones_ox = 0
    zeros_ox = 0
    ones_o2 = 0
    zeros_o2 = 0

    for row in ox:
        if row[iter] == '1':
            ones_ox += 1
        else:
            zeros_ox += 1

    for row in o2:
        if row[iter] == '1':
            ones_o2 += 1
        else:
            zeros_o2 += 1

    most1 = int(ones_ox >= zeros_ox)
    most2 = int(ones_o2 < zeros_o2)

    print(most2)
    if len(ox) == 1:
        pass
    else:
        ox = [elem for elem in ox if int(elem[iter]) == most1]
    if len(o2) == 1:
        pass
    else:
        o2 = [elem for elem in o2 if int(elem[iter]) == most2]
    print(o2)
    #print(o2)
    iter += 1
print(ox)
print(o2)
oxygen = int(ox[0], 2)
co2 = int(o2[0], 2)
print(oxygen)
print(co2)
print(oxygen * co2)
