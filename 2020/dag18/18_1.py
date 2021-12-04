import re
import sys
class tokenize:
    """docstring forTokenize."""

    def __init__(self, l):
        self.l = l
        self.token = 0

    def nextToken(self):
        if self.token < len(self.l)-1:
            self.token += 1

    def getToken(self):
        return self.l[self.token]

    def __str__(self):
        return str(self.l)

def operator(token):
    result = expression(token)
    while token.getToken() in ['+','*']:
        if token.getToken() == '+':
            token.nextToken()
            result += expression(token)
        else:
            token.nextToken()
            result *= expression(token)
    return result

def expression(token):
    #print(token.getToken())
    if token.getToken() == '(':
        token.nextToken() # pass (
        result = operator(token)
        token.nextToken() # pass )
    elif type(token.getToken()) == type(1):
        result = token.getToken()
        token.nextToken()
    return result

def convert(s):
    try:
        t = int(s)
    except Exception as e:
        t = s
    return t


with open(sys.argv[1], 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = data[:-1]

sum = 0
for row in data:

    l = re.split(" |", row)
    l = [c for c in l if c != '']
    l = list(map(convert,l))
    '''
    print(l)
    tkn = tokenize(l)
    print(tkn)
    print(tkn.getToken())
    tkn.nextToken()
    print(tkn.getToken())
    '''
    tkn = tokenize(l)
    sum += operator(tkn)

print(sum)
