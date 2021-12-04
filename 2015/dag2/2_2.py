with open('input2.txt','r') as f:
    data = f.readlines()

tot = 0
for row in data:
    l = list(map(int,row.split("x")))
    d = [2*(l[0]+l[1]), 2*(l[0]+l[2]), 2*(l[1]+l[2])]
    length = min(d) + l[0]*l[1]*l[2]
    tot += length

print(tot)
