with open('input2.txt','r') as f:
    data = f.readlines()

tot = 0
for row in data:
    l = list(map(int,row.split("x")))
    a = [l[0]*l[1], l[0]*l[2], l[1]*l[2]]
    area = min(a) + 2*a[0]+2*a[1]+2*a[2]
    tot += area

print(tot)
