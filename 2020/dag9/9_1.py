import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = list(map(int,data))

for i in range(25,len(data)):
    dat = data[i-25:i]
    ok = 0
    for j in range(len(dat)):
        for k in range(len(dat)):
            if j != k and dat[j] + dat[k] == data[i]:
                ok = (j,k)
    if ok == 0:
        print(data[i])
