import sys

def step(state, i_max, j_max):
    result = {}
    for i in range(i_max):
        for j in range(j_max):
            if (i, j) in state and state[(i, j)] == '>' and (i, (j+1)%j_max) not in state:
                result[(i, (j+1)%j_max)] = state[(i, j)]
            elif (i, j) in state:
                result[(i, j)] = state[(i, j)]
    
    next_result = {}
    for i in range(i_max):
        for j in range(j_max):
            if (i, j) in result and result[(i, j)] == 'v' and ((i+1)%i_max, j) not in result:
                next_result[((i+1)%i_max, j)] = result[(i, j)]
            elif (i, j) in result:
                next_result[(i, j)] = result[(i, j)]
    return next_result

def show(state, i_max, j_max):
    for i in range(i_max):
        for j in range(j_max):
            if (i, j) in state:
                print(state[(i, j)], end='')
            else:
                print('.', end='')
        print()
    print()

def check(state1, state2):
    for key in state1:
        if key in state2:
            if state1[key] != state2[key]:
                return False
        else:
            return False
    return True

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]


state = {}

i_max = len(data)
j_max = len(data[0])
for i, row in enumerate(data):
    for j, elem in enumerate(row):
        if elem == '>': state[(i, j)] = '>'
        if elem == 'v': state[(i, j)] = 'v'
prevstate = {}
n_iter = 0

print('Initial state:')
show(state, i_max, j_max)

while not check(state, prevstate):
    #print(n_iter)
    prevstate = state.copy()
    #print(prevstate)
    state = step(prevstate, i_max, j_max)
    n_iter += 1
    #print(f'After {n_iter} step{"s" if n_iter > 1 else ""}:')
    #show(state, i_max, j_max)

print(n_iter)
