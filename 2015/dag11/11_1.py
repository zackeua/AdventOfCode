import sys

def str_to_tup(s: str) -> tuple:
    data = [ord(c)-ord('a') for c in s]
    return tuple(data)

def tup_tp_str(t: tuple) -> str:
    data = [chr(n + ord('a')) for n in t]
    return ''.join(data)

def increasing(t: tuple) -> bool:
    for a, b, c in zip(t[:-2], t[1:-1], t[2:]):
        if (a+1 == b == c-1): return True
    return False

def two_pairs(t: tuple) -> bool:
    c = -1
    count = 0
    for a, b in zip(t[:-1], t[1:]):
        if (a == b and b != c):
            c = a
            count += 1
    return count > 1

def check_iol(t: tuple) -> bool:
    return (ord('i') - ord('a')) in t or \
           (ord('o') - ord('a')) in t or \
           (ord('l') - ord('a')) in t

def step(t: tuple) -> tuple:
    result = list(t)
    result[~0] += 1
    for i in range(1, len(result)):
        if result[~(i-1)] == ord('z') + 1:
            result[~(i-1)] = 0
            result[~i] += 1
        
        if result[~i] in {ord('i') - ord('a'), ord('o') - ord('a'), ord('l') - ord('a')}:
            return step( tuple(result[:~i] + [result[~i] + 1] + [0]*(i)))
    
    if result[0] == ord('z') + 1:
        result[0] = 0
        result[~0] += 1
    
    if result[~0] in {ord('i') - ord('a'), ord('o') - ord('a'), ord('l') - ord('a')}:
        return step(tuple(result[:~0] + [result[~0] + 1]))
    
    return tuple(result)

def next(s: str) -> str:
    password = str_to_tup(s)
    password = step(password)
    while not (increasing(password) and two_pairs(password)):
        password = step(password)
    
    return tup_tp_str(password)

with open(sys.argv[1], 'r') as f:
    data = f.readline()

print(next(data))
