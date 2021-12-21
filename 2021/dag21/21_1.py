import sys

state = [0,0]

def rand():
    state[0] = (state[0]%100) + 1
    state[1] += 1
    return state[0]


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]
    pos = [0, 0]
    data = [row.split(':') for row in data]
    pos[0] = int(data[0][1])-1
    pos[1] = int(data[1][1])-1


score = [0, 0]

player = 0
n_iter = 0

while score[0] < 1000 and score[1] < 1000:

    rolls = rand() + rand() + rand()

    pos[player] = (pos[player] + rolls)%10

    # add score
    score[player] += pos[player] + 1

    #print(rolls, pos[player], score[player])
    # flip player
    if player == 0:
        player = 1
    else:
        player = 0

print(score[player] * state[1])