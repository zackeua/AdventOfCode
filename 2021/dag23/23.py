import sys

from torch import gather

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


def flip(l, pos1, pos2):
    l[pos1[0]][pos1[1]] = l[pos2[0]][pos2[1]]
    l[pos2[0]][pos2[1]] = None

def dist(pos1, pos2):
    if pos1 == (0, 0) and pos2 == (1, 0): return 3
    if pos1 == (0, 0) and pos2 == (2, 0): return 4
    if pos1 == (0, 0) and pos2 == (1, 1): return 5
    if pos1 == (0, 0) and pos2 == (2, 1): return 6
    if pos1 == (0, 0) and pos2 == (1, 2): return 7
    if pos1 == (0, 0) and pos2 == (2, 2): return 8
    if pos1 == (0, 0) and pos2 == (1, 3): return 9
    if pos1 == (0, 0) and pos2 == (2, 3): return 10

    if pos1 == (0, 1) and pos2 == (1, 0): return 2
    if pos1 == (0, 1) and pos2 == (2, 0): return 3
    if pos1 == (0, 1) and pos2 == (1, 1): return 4
    if pos1 == (0, 1) and pos2 == (2, 1): return 5
    if pos1 == (0, 1) and pos2 == (1, 2): return 6
    if pos1 == (0, 1) and pos2 == (2, 2): return 7
    if pos1 == (0, 1) and pos2 == (1, 3): return 8
    if pos1 == (0, 1) and pos2 == (2, 3): return 9

    if pos1 == (0, 2) and pos2 == (1, 0): return 2
    if pos1 == (0, 2) and pos2 == (2, 0): return 3
    if pos1 == (0, 2) and pos2 == (1, 1): return 2
    if pos1 == (0, 2) and pos2 == (2, 1): return 3
    if pos1 == (0, 2) and pos2 == (1, 2): return 4
    if pos1 == (0, 2) and pos2 == (2, 2): return 5
    if pos1 == (0, 2) and pos2 == (1, 3): return 6
    if pos1 == (0, 2) and pos2 == (2, 3): return 7

    if pos1 == (0, 3) and pos2 == (1, 0): return 4
    if pos1 == (0, 3) and pos2 == (2, 0): return 5
    if pos1 == (0, 3) and pos2 == (1, 1): return 2
    if pos1 == (0, 3) and pos2 == (2, 1): return 3
    if pos1 == (0, 3) and pos2 == (1, 2): return 2
    if pos1 == (0, 3) and pos2 == (2, 2): return 3
    if pos1 == (0, 3) and pos2 == (1, 3): return 4
    if pos1 == (0, 3) and pos2 == (2, 3): return 5

    if pos1 == (0, 4) and pos2 == (1, 0): return 6
    if pos1 == (0, 4) and pos2 == (2, 0): return 7
    if pos1 == (0, 4) and pos2 == (1, 1): return 4
    if pos1 == (0, 4) and pos2 == (2, 1): return 5
    if pos1 == (0, 4) and pos2 == (1, 2): return 4
    if pos1 == (0, 4) and pos2 == (2, 2): return 5
    if pos1 == (0, 4) and pos2 == (1, 3): return 2
    if pos1 == (0, 4) and pos2 == (2, 3): return 3

    if pos1 == (0, 5) and pos2 == (1, 0): return 8
    if pos1 == (0, 5) and pos2 == (2, 0): return 9
    if pos1 == (0, 5) and pos2 == (1, 1): return 6
    if pos1 == (0, 5) and pos2 == (2, 1): return 7
    if pos1 == (0, 5) and pos2 == (1, 2): return 6
    if pos1 == (0, 5) and pos2 == (2, 2): return 7
    if pos1 == (0, 5) and pos2 == (1, 3): return 2
    if pos1 == (0, 5) and pos2 == (2, 3): return 3

    if pos1 == (0, 6) and pos2 == (1, 0): return 9
    if pos1 == (0, 6) and pos2 == (2, 0): return 10
    if pos1 == (0, 6) and pos2 == (1, 1): return 7
    if pos1 == (0, 6) and pos2 == (2, 1): return 8
    if pos1 == (0, 6) and pos2 == (1, 2): return 7
    if pos1 == (0, 6) and pos2 == (2, 2): return 8
    if pos1 == (0, 6) and pos2 == (1, 3): return 3
    if pos1 == (0, 6) and pos2 == (2, 3): return 4

    return dist(pos2, pos1)

    # #print(pos1, pos2)
    # #input()
    # if pos1 == pos2:
    #     return 0
    
    # if pos1[0] < pos2[0]:
    #     return dist(pos2, pos1)
    # elif pos1[0] == 2:
    #     return 1 + dist((1, pos1[1]) , pos2)
    # elif pos1[0] == 1:
    #     return 2 + dist((0, pos1[1] + (1 if pos1[1] < pos2[1] else -1)), pos2)
    # else:
    #     if pos1[1] == 0 or (pos1[1] == 5 and pos2[1] == 6):
    #         return 1 + dist((pos1[0], pos1[1] + 1), pos2)
    #     elif pos1[1] == 6 or (pos1[1] == 1 and pos2[1] == 0):
    #         return 1 + dist((pos1[0], pos1[1] - 1), pos2)
    #     else:
    #         return 2 + dist((pos1[0], pos1[1] + (1 if pos1[1] < pos2[1] else -1)), pos2)

def cost(t, pos1, pos2):
    n = t[pos1[0]][pos1[1]]
    #print(pos1, pos2, n, dist(pos1, pos2))
    return 10**n * dist(pos1, pos2)

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
        for j in range(0, 4):
            empty[(i, j)] = s[i][j] == None
            if not empty[(i, j)] and not inCorrectPos(s, (i, j)):
                pieces.append((i, j))

    for piece in pieces:
        if piece[0] == 0: # if piece in hallway move it into room
            # check for blocked way to room entrence:

            # index of where piece wants to move
            val = s[piece[0]][piece[1]]

            free_path = True
            if piece[1] < val + 1: # one under pos where piece wants to move, iterate from piece to that position
                for i in range(piece[1]+1, val + 2):
                    free_path = free_path and empty[(0, i)]
            elif val + 2 < piece[1]:
                for i in range(val+2, piece[1]):
                    free_path = free_path and empty[(0, i)]
            
            if free_path and s[1][s[piece[0]][piece[1]]] == None and s[2][s[piece[0]][piece[1]]] == None:
                # add (2, s[piece[0]][piece[1]]) to possible paths
                l = to_list(s)
                flip(l, (2, s[piece[0]][piece[1]]), piece)
                c = cost(l, (2, s[piece[0]][piece[1]]), piece)
                return [(to_tup(l), c)]

            elif free_path and s[1][s[piece[0]][piece[1]]] == None and s[2][s[piece[0]][piece[1]]] == s[piece[0]][piece[1]]:
                # add (1, s[piece[0]][piece[1]]) to possible paths
                l = to_list(s)
                flip(l, (1, s[piece[0]][piece[1]]), piece)
                c = cost(l, (1, s[piece[0]][piece[1]]), piece)
                return [(to_tup(l), c)]

        elif piece[0] == 1:
            free_path = True
            for i in range(piece[1] + 2, 7):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, i)]
                    if free_path:
                        l = to_list(s)
                        flip(l, (0, i), piece)
                        c = cost(l, (0, i), piece)
                        moves.append((to_tup(l), c))
            free_path = True
            for i in range(piece[1] + 1, -1, -1):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, i)]
                    if free_path:
                        l = to_list(s)
                        flip(l, (0, i), piece)
                        c = cost(l, (0, i), piece)
                        moves.append((to_tup(l), c))
        elif piece[0] == 2:
            free_path = empty[(1, piece[1])]
            for i in range(piece[1] + 2, 7):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, i)]
                    if free_path:
                        l = to_list(s)
                        flip(l, (0, i), piece)
                        c = cost(l, (0, i), piece)
                        moves.append((to_tup(l), c))
            free_path = empty[(1, piece[1])]
            for i in range(piece[1] + 1, -1, -1):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, i)]
                    if free_path:
                        l = to_list(s)
                        flip(l, (0, i), piece)
                        c = cost(l, (0, i), piece)
                        moves.append((to_tup(l), c))
    #print(moves)
    #input()
    return moves



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

for i in range(len(goal[0])):
    goal[0][i] = None

for i in range(len(goal[1])):
    goal[1][i] = i

for i in range(len(goal[2])):
    goal[2][i] = i

goal = to_tup(goal)


show(data)
show(goal)

g = {}
Q = [data]
V = []
g[goal] = (float('inf'), None)
g[data] = (0, None)

n_iter = 0

while Q != []:
    us = [(s, g[s][0]) for s in Q]
    us.sort(key=lambda t: t[1])
    #print(f'iter: {n_iter}')
    #n_iter += 1
    #for key in g:
    #    print(g[key])
    #    show(key)
    #input()
    u = us[0][0]
    Q.remove(u)
    V.append(u)
    if u == goal:
        print('here')
        break
    moves = valid_moves(u)

    Q.extend([move for move, _ in moves if move not in V])

    for move, c in moves:

        if move not in V:
            cc = g[u][0] + c
            if move in g and cc < g[move][0] or move not in g:
                g[move] = (cc, u)
    # for elem in g:
    #     show(elem)
    #     print(g[elem])
    # input()

print(g[goal])


show_moves(g, goal)

print(g[goal][0])
