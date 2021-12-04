import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()

dat = []

for row in data:
    dat.append([0, row])

acc = 0

ip = 0

while ip < len(dat):
    row = dat[ip]
    if row[0] == 1:
        print(acc)
        break
    row[0] += 1
    if row[1][:3] == "acc":
        acc += int(row[1][3:])
    if row[1][:3] == "jmp":
        ip += int(row[1][3:])-1
    ip += 1
