import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()

ids = []

for row in data:
    row = row[:-1]
    row_l = 0
    row_u = 127
    col_l = 0
    col_u = 7

    for c in row:
        if c == "F":
            row_u = (row_l + row_u)//2
        if c == "B":
            row_l = (row_l + row_u)//2
        if c == "R":
            col_l = (col_l + col_u)//2
        if c == "L":
            col_u = (col_l + col_u)//2
    ID = row_u * 8 + col_u
    ids.append(ID)

ids.sort()

for i, id in enumerate(ids[:-1]):
    if id+1 != ids[i+1]:
        print(id+1)
