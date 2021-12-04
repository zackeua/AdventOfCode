import sys
with open(sys.argv[1], 'r') as f:
    data = f.read().split('\n\n')

total = 0
for group in data:
    individuals = group.split('\n')
    if individuals[-1] == "":
        individuals = individuals[:-1]
    #print(individuals)
    local = 0
    for c in "abcdefghijklmnopqrstuvwxyz":
        cc = 1
        for individual in individuals:
            if c not in individual:
                cc = 0
        local += cc == 1
    total += local

print(total)
