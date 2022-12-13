import sys
from functools import lru_cache
import heapq

def to_list(tup):
    return [list(row) for row in tup]

def to_tup(l):
    return tuple([tuple(elem) for elem in l])

def flip(l, pos1, pos2):
    c = l[pos2[0]][pos2[1]]
    l[pos2[0]][pos2[1]] = None
    l[pos1[0]][pos1[1]] = c
    return l


def show(t):
    print('#############')
    for row in t[:2]:
        print('#', end='')
        for elem in row:
            if elem != None: print(chr(elem - 1 + ord('A')), end='')
            else: print('.', end='')
        print('#')
        
    for row in t[2:]:
        print(' ', end='')
        for elem in row:
            if elem != None: print(chr(elem - 1 + ord('A')), end='')
            else: print('.', end='')
        print('#')
    print('  #########\n')

def show_moves(g, goal):
    if goal == None: return
    if g[goal][1] == None:
        show_moves(g, g[goal][1])
        print(f'Cost: 0')
        show(goal)
    else:
        show_moves(g, g[goal][1])
        print(f'+ {g[goal][0] - g[g[goal][1]][0]}')
        print(f'Cost: {g[goal][0]}')
        show(goal)

def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def cost(t, pos1, pos2):
    n = t[pos2[0]][pos2[1]]
    return 10**(n-1) * dist(pos1, pos2)
    

def inCorrectPos(l, pos):
    if l[pos[0]][pos[1]] in (1,2,3,4):
        y = l[pos[0]][pos[1]]*2
        return pos == (1, y) and l[2][y] == l[pos[0]][pos[1]] or pos == (2, y)
    return False


@lru_cache(maxsize=None)
def valid_moves(s):
    empty = {}
    pieces = []
    moves = []
    for i in range(0, 11):
        empty[(0, i)] = s[0][i] == None
        if not empty[(0, i)] and not inCorrectPos(s, (0, i)): pieces.append((0, i))
        
    for i in range(1, 3):
        for j in range(2, 9, 2):
            empty[(i, j)] = s[i][j] == None
            if not empty[(i, j)] and not inCorrectPos(s, (i, j)): pieces.append((i, j))
    
    for piece in pieces:
        #if not inCorrectPos(s, piece): # dont touch pieces in the correct room
        if piece[0] == 0: # if piece in hallway move it into room
            # check for blocked way to room entrence:
            end = (0, s[piece[0]][piece[1]]*2)
            begin = min([piece[1], end[1]])
            last = max([piece[1], end[1]])+1
            free_path = True
            for i in range(begin, last):
                if (0, i) != piece: free_path = free_path and empty[(0, i)]
            
            # Check for empty room and move it as far into the room as possible:
            if free_path and s[1][end[1]] == None and s[2][end[1]] == None:
                # add (3, end[1]) to possible paths
                
                l = to_list(s)
                c = cost(l, (2, end[1]), piece)              
                l = flip(l, (2, end[1]), piece)
                return [(c, to_tup(l))]
        
            elif free_path and s[1][end[1]] == None and s[2][end[1]] == s[piece[0]][piece[1]]:
                # add (2, end[1]) to possible paths
                l = to_list(s)
                c = cost(l, (1, end[1]), piece)
                l = flip(l, (1, end[1]), piece)
                return [(c, to_tup(l))]

        elif piece[0] == 1:
            free_path = True
            for i in range(piece[1], 11):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, i)]
                    if free_path and (i%2==1 or i == 10):
                        l = to_list(s)
                        c = cost(l, (0, i), piece)
                        l = flip(l, (0, i), piece)
                        moves.append((c, to_tup(l)))
            free_path = True
            for i in range(piece[1], -1, -1):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, piece[1]-i)]
                    if free_path and (i%2==1 or i == 0):
                        l = to_list(s)
                        c = cost(l, (0, i), piece)
                        l = flip(l, (0, i), piece)
                        moves.append((c, to_tup(l)))

        elif piece[0] == 2:
            free_path = empty[(1, piece[1])]
            for i in range(piece[1], 11):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, i)]
                    if free_path and (i%2==1 or i == 10):
                        #add (0, piece[1]+i) to possible paths
                        l = to_list(s)
                        c = cost(l, (0, i), piece)
                        l = flip(l, (0, i), piece)
                        moves.append((c, to_tup(l)))
            
            free_path = empty[(1, piece[1])]
            for i in range(piece[1], -1, -1):
                if (0, i) in empty:
                    free_path = free_path and empty[(0, i)]
                    if free_path and (i%2==1 or i == 0):
                        #add (0, piece[1]-i) to possible paths
                        l = to_list(s)
                        c = cost(l, (0, i), piece)
                        l = flip(l, (0, i), piece)
                        moves.append((c, to_tup(l)))
    #moves = [("#############\n#A..........#\n###.#B#C#D###\n  #A#B#C#D#\n  #########", 0)]

    return moves



with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    #data = "#############\n#...........#\n###B#C#B#D###\n  #A#D#C#A#\n  #########"
    data = [row.replace('\n', '') for row in data]
    #show(data)



data = data[1:-1]
data = [[None if elem =='.' else ord(elem)-ord('A')+1 for elem in row[1:-1]] for row in data]

data = to_tup(to_list(data))

goal = to_list(data)


for i, row in enumerate(goal):
    if  0 < i < 3:
        for j, elem in enumerate(row):
            if j != 0 and j != 10 and j%2 == 0: goal[i][j] = j//2
for i, elem in enumerate(goal[0]):
    goal[0][i] = None

goal = to_tup(goal)


#data = "#############\n#...........#\n###B#B#C#D###\n  #A#A#C#D#\n  #########"
g = {}
Q = [data]
V = set()
#g[goal] = (float('inf'), None)
g[data] = (0, None)

heap = []
heapq.heappush(heap, (0, 0, data))
#print(g)
n_iter = 0
num_items = 0
while heap != []:
    n_iter += 1

    heapq.heapify(heap)
    u = heapq.heappop(heap)
    
    
    if u[2] == goal:
        print('here')
        break
    moves = valid_moves(u[2])
    
    V.add(u[2])
    
    for c, move in moves:
        
        if move not in V:
            cc = g[u[2]][0] + c
            #print('ff', cc)
            if move in g and cc < g[move][0] or move not in g:
                
                g[move] = (cc, u[2])
            num_items += 1
            heapq.heappush(heap, (cc, num_items, move))
            
    
#print(g)
print(g[goal])


show_moves(g, goal)

print(g[goal][0])
'''
u = goal

while g[u][1] != None:
    show(u)
    u = g[u][1]

show(u)
'''
