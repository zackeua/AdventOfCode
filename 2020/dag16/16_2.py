import re
import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()


rulesUpper = []
rulesLower = []
tickets = []
valid = []
invalid = []

newline = "\n"

for row in data:
    if row == "\n":
        break
    text = re.sub("[ a-zA-Z]+: ","",row)
    p1, p2 = text.split(" or ")
    pl1, pu1 = p1.split('-')
    pl2, pu2 = p2.split('-')
    rulesLower.append(int(pl1))
    rulesUpper.append(int(pu1))

    rulesLower.append(int(pl2))
    rulesUpper.append(int(pu2))

pass1 = False
pass2 = False
pass3 = False
pass4 = False
for row in data:

    if pass1:
        pass2 = True
    if row == "nearby tickets:\n":
        pass1 = True

    if pass3:
        pass4 = True
    if row == "your ticket:\n":
        pass3 = True

    if pass4:
        myTicket = list(map(int,row.split(',')))
        pass3 = False
        pass4 = False

    if pass2:
        tickets.append(row)


print(myTicket)

for t, row in enumerate(tickets):
    for num in list(map(int,row.split(','))):
        passing = False
        for i, rule in enumerate(rulesUpper):
            if passing == False and rulesLower[i] <= num <= rule:
                passing = True
        if passing == False:
            if len(invalid) == 0:
                invalid.append(t)
            elif invalid[-1] != t:
                invalid.append(t)

valid = [ticket for i, ticket in enumerate(tickets) if i not in invalid]

for i in range(len(valid)):
    valid[i] = list(map(int,valid[i].split(',')))
    #print(valid[i])



possible = [[] for _ in range(len(rulesLower)//2)]

for rule in range(len(rulesLower)//2):
    for position in range(len(valid[0])):
        passing = True
        for ticket in range(len(valid)):
            num = valid[ticket][position]
            #print(f'')
            if (not ((rulesLower[rule*2] <= num <= rulesUpper[rule*2]) or (rulesLower[rule*2+1] <= num <= rulesUpper[rule*2+1]))):
                passing = False
        #possible[rule].append(position)
        if passing:
            possible[rule].append(position)

#print(possible)

minimal = False

while not minimal:
    for i in range(len(possible)):
        if len(possible[i]) == 1:
            for j in range(len(possible)):
                if i != j:
                    if possible[i][0] in possible[j]:
                        possible[j].remove(possible[i][0])
    minimal = True
    for row in possible:
        if len(row) != 1:
            minimal = False

#print(possible)

res = 1
for i in range(6):
    res *= myTicket[possible[i][0]]

print(res)
