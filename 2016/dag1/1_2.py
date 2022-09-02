import sys

with open(sys.argv[1], 'r') as f:
    data = [(l[0], int(l[1:])) for l in f.readline().split(', ')]
    print(data)

position = [(0, 0)]

state = 0


for turn, step in data:
    if turn == 'R':
        state = (state + 1) % 4
    else:
        state = (state - 1) % 4

    for _ in range(step):
        if state == 0:
            pos = (position[-1][0] + 1, position[-1][1])
        elif state == 1:
            pos = (position[-1][0], position[-1][1] + 1)
        elif state == 2:
            pos = (position[-1][0] - 1, position[-1][1])
        else:
            pos = (position[-1][0], position[-1][1] - 1)

        if pos in position:
            print(abs(pos[0]) + abs(pos[1]))
            print(pos)
            exit()

        position.append(pos)


