import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    state = [[int(elem) for elem in row if elem != '\n'] for row in data]

def increment(state):
    result = []
    flashed = []
    tot_flashed = 0
    for i, row in enumerate(state):
        temp_row = []
        for j, elem in enumerate(row):
            temp_row.append((elem+1)%10)
            if elem == 9:
                flashed.append((i,j))
                tot_flashed += 1
        result.append(temp_row)
    return result, flashed, tot_flashed

def increment_neigh(state, flashed):
    result = state.copy()
    tot_flashed = 0
    while len(flashed) != 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= flashed[0][0]+i < len(state) and 0 <= flashed[0][1]+j < len(state[0]) and result[flashed[0][0]+i][flashed[0][1]+j] != 0:
                    result[flashed[0][0]+i][flashed[0][1]+j] += 1
                    if result[flashed[0][0]+i][flashed[0][1]+j] == 10:
                        result[flashed[0][0]+i][flashed[0][1]+j] = 0
                        flashed.append((flashed[0][0]+i, flashed[0][1]+j))
                        tot_flashed += 1
        flashed = flashed[1:]
    return result, tot_flashed

def step(state, tot_flashed):
    tot = tot_flashed
    state, flashed, temp_flashed = increment(state)
    tot += temp_flashed

    state, temp_flashed = increment_neigh(state, flashed)
    tot += temp_flashed
    return state, tot

steps = 0
tot_flashed = 0
print(state)
while True:
    state, next_flashed = step(state, tot_flashed)
    steps += 1
    if next_flashed - tot_flashed == len(state) * len(state[0]):
        break


print(state)
for row in state:
    print(row)

print(steps)