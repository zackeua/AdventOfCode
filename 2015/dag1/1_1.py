with open('input1.txt','r') as f:
    data = f.readlines()

floor = 0

for row in data:
    for c in row:
        if c == "(":
            floor += 1
        if c == ")":
            floor -= 1

print(floor)
