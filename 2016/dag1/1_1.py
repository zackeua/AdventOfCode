import sys

with open(sys.argv[1], 'r') as f:
    data = [(l[0], int(l[1:])) for l in f.readline().split(', ')]
    print(data)

position = (0, 0)

state = 0


for turn, step in data:
    if turn == 'R':
        state = (state + 1) % 4
    else:
        state = (state - 1) % 4

    if state == 0:
        position = (position[0] + step, position[1])
    elif state == 1:
        position = (position[0], position[1] + step)
    elif state == 2:
        position = (position[0] - step, position[1])
    else:
        position = (position[0], position[1] - step)


print(abs(position[0]) + abs(position[1]))