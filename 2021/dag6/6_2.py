import sys


def step(state):
    result = [0]*9
    result[6] = state[0]
    result[0] = state[1]
    result[1] = state[2]
    result[2] = state[3]
    result[3] = state[4]
    result[4] = state[5]
    result[5] = state[6]
    result[6] += state[7]
    result[7] = state[8]
    result[8] = state[0]
    return result


with open(sys.argv[1], 'r') as f:
    age = list(map(int, f.readline().split(',')))
state = [age.count(i) for i in range(9)]
n_iter = 0
while n_iter < 256:
    state = step(state)
    n_iter += 1

print(sum(state))
