import re
import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()


rulesUpper = []
rulesLower = []


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
count = 0
for row in data:
    if pass1:
        pass2 = True
    if row == "nearby tickets:\n":
        pass1 = True

    if pass2:
        for num in list(map(int,row.split(','))):
            passing = False
            for i, rule in enumerate(rulesUpper):
                if passing == False and rulesLower[i] <= num <= rule:
                    passing = True
            if passing == False:
                count += num
print(count)
