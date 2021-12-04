import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()

i = 0
j = 0
jl = len(data[0])-1
count = 0
while i < len(data):
        count += data[i][j%jl] == "#"
        i += 1
        j += 3
print(count)
