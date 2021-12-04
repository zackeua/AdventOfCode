with open('input3.txt','r') as f:
    data = f.read()


i = 0;
j = 0;
d = {}

d[i] = {}
d[i][j] = 1
for c in data:
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

tot = 0

for key1 in list(d.keys()):
    tot += len(list(d[key1].keys()))

print(tot)
