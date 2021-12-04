with open('input7.txt', 'r') as f:
    data = f.readlines()
    d = {}
    dd = {}
    for row in data:
        dat = row.split(' -> ')
        dat[0] = dat[0].strip()
        dat[1] = dat[1].strip()
        d[dat[1]] = dat[0]
        dd[dat[1]] = dat[0]


def get(c):
    if c not in d:
        return int16(int(c))
    #print(d[c])
    if type(d[c]) == int16:
        pass
    elif 'NOT' in d[c]:
        args = d[c].split()
        d[c] = get(args[1]).__invert__()
    elif 'AND' in d[c]:
        args = d[c].split(' AND ')
        d[c] = get(args[0]).__and__(get(args[1]))
    elif 'OR' in d[c]:
        args = d[c].split(' OR ')
        d[c] = get(args[0]).__or__(get(args[1]))
    elif 'LSHIFT' in d[c]:
        args = d[c].split(' LSHIFT ')
        d[c] = get(args[0]).LSHIFT(int(args[1]))
    elif 'RSHIFT' in d[c]:
        args = d[c].split(' RSHIFT ')
        d[c] = get(args[0]).RSHIFT(int(args[1]))
    elif d[c].isnumeric():
        d[c] = int16(int(d[c]))
    else:
        d[c] = get(d[c])
    return d[c]

class int16:
    """docstring for INTEGER."""


    def __init__(self, arg=None):
        self._bytes = [0]*16
        if arg != None:
            power = 2**15
            i = 0
            arr = arg
            while arr > 0:
                self._bytes[i] = arr//power
                arr = arr - self._bytes[i]*power
                power = power//2
                #print(f'i = {i}, power = {power}, value = {self._bytes[i]}, rest = {arr}')
                i += 1
    def __and__(self, arg):
        res = int16()
        for i, (b1, b2) in enumerate(zip(self._bytes, arg._bytes)):
            res._bytes[i] = b1 and b2
        return res

    def __or__(self, arg):
        res = int16()
        for i, (b1, b2) in enumerate(zip(self._bytes, arg._bytes)):
            res._bytes[i] = b1 or b2
        return res

    def LSHIFT(self, arg):
        res = int16()
        for i, b1 in enumerate(self._bytes[arg:]):
            res._bytes[i] = b1
        return res

    def RSHIFT(self, arg):
        res = int16()
        for i, b1 in enumerate(self._bytes[:-arg], arg):
            res._bytes[i] = b1
        return res

    def __invert__(self):
        res = int16()
        for i, b1 in enumerate(self._bytes):
            res._bytes[i] = not b1
        return res

    def toInt(self):
        power = 2**15
        res = 0
        for val in self._bytes:
            res += power * val
            power = power // 2
        return res

    def __str__(self):
        return str(self.toInt())


#print(int16(4).RSHIFT(4))
#print(int16(123).__invert__())

for key in d.keys():
    get(key)
    print(f'{key}: {d[key]}')

b = get('a')
print(b)
d = dd
d['b'] = b
print(get('a'))
