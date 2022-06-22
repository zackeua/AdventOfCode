import sys

def inc(state, val, ptr):
    state[val] += 1
    ptr[0] += 1

def hlf(state, val, ptr):
    state[val] = state[val]//2
    ptr[0] += 1

def tpl(state, val, ptr):
    state[val] *= 3
    ptr[0] += 1

def jmp(offset, ptr):
    ptr[0] += int(offset)

def jie(state, val, offset, ptr):
    if state[val]%2 == 0:
        ptr[0] += int(offset)
    else:
        ptr[0] += 1
def jio(state, val, offset, ptr):
    if state[val] == 1:
        ptr[0] += int(offset)
    else:
        ptr[0] += 1

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [l.strip('\n') for l in data]

ptr = [0]

state = {'a': 0, 'b': 0}

print(data)

while 0 <= ptr[0] < len(data):
    #print(data[ptr[0]][:3])
    #print(ptr[0])
    if data[ptr[0]][:3] == 'inc':
        inc(state, data[ptr[0]][4], ptr)
    elif data[ptr[0]][:3] == 'hlf':
        hlf(state, data[ptr[0]][4], ptr)
    elif data[ptr[0]][:3] == 'tpl':
        tpl(state, data[ptr[0]][4], ptr)
    elif data[ptr[0]][:3] == 'jmp':
        jmp(int(data[ptr[0]][4:]), ptr)
    elif data[ptr[0]][:3] == 'jie':
        jie(state, data[ptr[0]][4], int(data[ptr[0]][7:]), ptr)
    elif data[ptr[0]][:3] == 'jio':
        jio(state, data[ptr[0]][4], int(data[ptr[0]][7:]), ptr)
    
print(state['b'])