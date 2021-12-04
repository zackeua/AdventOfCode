from functools import reduce
import sys
def modInverse(a,m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a//m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if x < 0:
        x = x + m0
    return x


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    travelTime = int(data[0])
    lines = data[1].split(',')
    lines = [[pos, int(line)] for pos, line in enumerate(lines) if 'x' not in line]

m = [l[1] for l in lines]

offset = [l[0] for l in lines]


# kinesiska modulo teoremet
print(lines)
M = reduce((lambda x1, x2: x1*x2), m)
print(f'M = {M}')
M_i = [int(M/m_i) for m_i in m]
invM_i = [0 for _ in M_i]
for i, m_i in enumerate(M_i):
    print(f'm_{i} = {m_i}')
    invM_i[i] = modInverse(m_i, m[i])

print(sum(-offset[i]*m_i*invM_i[i] for i, m_i in enumerate(M_i))%M)
