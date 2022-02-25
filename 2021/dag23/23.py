import sys

k = {}

def to_list(tup):
    return [list(row) for row in tup]


def to_tup(l):
    return tuple([tuple(elem) for elem in l])

def print_elem(elem, c='.', e='.'):
    if elem != None:
        print(chr(elem + ord('A')), end=e)
    else:
        print(c, end=e)

def show(t):
    print('#############')
    print('#', end='')
    for elem in t[0][:2]:
        print_elem(elem, e='')
    print('.', end='')
    for elem in t[0][2:5]:
        print_elem(elem)    
    for elem in t[0][5:]:
        print_elem(elem, e='')    
    print('#')
    print('###', end='')
    for elem in t[1]:
        print_elem(elem, e='#')
    print("##")
    print('  #', end='')
    for elem in t[2]:
        print_elem(elem, e='#')
    print()
    print('  #########')


def show_moves(g, goal):
    if goal == None:
        return
    if g[goal][1] == None:
        show_moves(g, g[goal][1])
        print(f'Cost: 0')
        show(goal)
    else:
        show_moves(g, g[goal][1])
        print(f'+ {g[goal][0] - g[g[goal][1]][0]}')
        print(f'Cost: {g[goal][0]}')
        show(goal)


def inCorrectPos(l, pos):
    if l[pos[0]][pos[1]] in (0, 1, 2, 3):
        y = l[pos[0]][pos[1]]
        return pos == (1, y) and l[2][y] == l[pos[0]][pos[1]] or pos == (2, y)
    return False

def valid_moves(s):
    if s in k:
        return k[s]
    empty = {}
    pieces = []
    moves = []

    for i in range(0, 7):
        empty[(0, i)] = s[0][i] == None
        if not empty[(0, i)] and not inCorrectPos(s, (0, i)):
            pieces.append((0, i))

    for i in range(1, 3):
        for j in range(0, 5):
            empty[(i, j)] = s[i][j] == None
            if not empty[(i, j)] and not inCorrectPos(s, (i, j)):
                pieces.append((i, j))

    for piece in pieces:
        if piece[0] == 0: # if piece in hallway move it into room
             # check for blocked way to room entrence:
    

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    #data = "#############\n#...........#\n###B#C#B#D###\n  #A#D#C#A#\n  #########"
    data = [row.replace('\n', '') for row in data]
    #show(data)
    
print(data)
data = data[1:-1]
data = [[None if elem == '.' else ord(elem)-ord('A') for elem in row[1:-1]] for row in data]
print(data)

data = [data[0][:2] + data[0][3:-2:2] +data[0][-2:], data[1][2:9:2], data[2][2:9:2]]
print(data)
data = to_tup(to_list(data))

goal = to_list(data)

show(data)