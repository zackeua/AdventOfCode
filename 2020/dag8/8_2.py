import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()

dat = []

for row in data:
    dat.append([0, row])


l = []


for i, row in enumerate(dat):
    if row[1][:3] == "nop":
        l.append(i)
    if row[1][:3] == "jmp":
        l.append(i)


for elem in l:
    i = elem
    lo = 1
    d = dat.copy()
    acc = 0
    ip = 0
    while ip < len(d) and lo==1:
        row = d[ip]
        if i != ip:
            if row[0] == 1:
                lo = 0
            row[0] += 1
            if row[1][:3] == "acc":
                acc += int(row[1][3:])
            if row[1][:3] == "jmp":
                ip += int(row[1][3:])-1
            ip += 1
        else:
            if row[0] == 1:
                lo = 0
            row[0] += 1
            if row[1][:3] == "acc":
                acc += int(row[1][3:])
            if row[1][:3] == "nop":
                ip += int(row[1][3:])-1
            ip += 1
    if lo == 1:
        print(acc)
        break
