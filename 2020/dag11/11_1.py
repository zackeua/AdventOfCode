import sys
def occupied(L,i,j):
    tot = 0

    if i > 0:
        tot += L[(i-1)][j] == "#"
        if j > 0:
            tot += L[(i-1)][(j-1)] == "#"
        if j < len(L[0])-1:
            tot += L[(i-1)][(j+1)] == "#"

    if i < len(L)-1:
        tot += L[(i+1)][j] == "#"
        if j > 0:
            tot += L[(i+1)][(j-1)] == "#"
        if j < len(L[0])-1:
            tot += L[(i+1)][(j+1)] == "#"

    #tot += L[i][j] == "#"
    if j > 0:
        tot += L[i][(j-1)] == "#"
    if j < len(L[0])-1:
        tot += L[i][(j+1)] == "#"

    return tot

def disp(L):
    for row in L:
        for c in row:
            print(c,end="")
        print()
    print()
    print()

def copy(L):
    l = []
    for row in L:
        temp = []
        for c in row:
            temp.append(c)
        l.append(temp)
    return l


with open(sys.argv[1], 'r') as f:
    inp = f.read()
    inp = inp.split("\n")
    inp = inp[:-1]

data = [[c for c in row] for row in inp]
data = [copy(data), copy(data)]


current = 0
disp(data[current])
changed = 1

while changed:
    changed = 0
    prev = current
    current = (current+1)%2
    for i in range(len(data[0])):
        for j in range(len(data[0][0])):
            tot = occupied(data[prev],i,j)
            if data[prev][i][j] == "L" and tot == 0:
                data[current][i][j] = "#"
                changed = 1
            elif data[prev][i][j] == "#" and tot >= 4:
                data[current][i][j] = "L"
                changed = 1
            else:
                data[current][i][j] = data[prev][i][j]
    disp(data[current])


count = 0
for i in range(len(data[0])):
    for j in range(len(data[0][0])):
        count += data[current][i][j] == "#"
print(count)
