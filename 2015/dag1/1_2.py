with open('input1.txt','r') as f:
    data = f.readlines()

floor = 0
i = 0
for row in data:
    for c in row:
        i += 1
        if c == "(":
            floor += 1
        if c == ")":
            floor -= 1
        if floor < 0:
            print(i)
            break;
            
