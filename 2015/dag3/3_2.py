with open('input3.txt','r') as f:
    data = f.read()


i_1 = 0;
j_1 = 0;
i_2 = 0;
j_2 = 0;
d = {}

d[i_1] = {}
d[i_1][j_1] = 1
santa = True
for c in data:
    if santa:
        i = i_1
        j = j_1
    else:
        i = i_2
        j = j_2

    if c == 'v':
        i -= 1
    elif c == '^':
        i += 1
    elif c == '<':
        j -= 1
    elif c == '>':
        j += 1

    if i not in d:
        d[i] = {}
    if j not in d[i]:
        d[i][j] = 1

    if santa:
        i_1 = i
        j_1 = j
    else:
        i_2 = i
        j_2 = j
    santa = not santa

tot = 0

for key1 in list(d.keys()):
    tot += len(list(d[key1].keys()))

print(tot)
