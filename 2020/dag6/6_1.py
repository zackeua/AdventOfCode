import sys
with open(sys.argv[1],'r') as f:
    data = f.read().split('\n\n')

#import sys
#data = '\n'.join(list(sys.stdin)).split('\n\n')


total = 0
for group in data:
    individuals = group.split('\n')
    local = 0
    for c in "abcdefghijklmnopqrstuvwxyz":
        cc = 0
        for individual in individuals:
            if c in individual:
                cc = 1
        local += cc == 1
    print(local)
    total += local

print(total)
