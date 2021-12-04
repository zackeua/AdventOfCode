import sys
with open(sys.argv[1],'r') as f:
    data = f.readlines()

il = len(data)
jl = len(data[0])-1
total = 1

i = 0
j = 0
count = 0

while i < il:
        count += data[i][j%jl] == "#"
        i += 1
        j += 1
total *= count
print(count)
count = 0
i = 0
j = 0

while i < il:
        count += data[i][j%jl] == "#"
        i += 1
        j += 3
total *= count
print(count)
count = 0
i = 0
j = 0

while i < il:
    count += data[i][j%jl] == "#"
    i += 1
    j += 5
total *= count
print(count)
count = 0
i = 0
j = 0

while i < il:
    count += data[i][j%jl] == "#"
    i += 1
    j += 7
total *= count
print(count)
count = 0
i = 0
j = 0

while i < il:
    count += data[i][j%jl] == "#"
    i += 2
    j += 1
total *= count
print(count)

print(total)
