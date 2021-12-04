with open('input6.txt','r') as f:
    data = f.readlines()

grid = [[False for _ in range(1000)] for _ in range(1000)]



for row in data:

    if "turn on" in row:
        s = row[8:]
        s = s.split('through')
        s[0] = s[0].split(',')
        s[1] = s[1].split(',')
        for x in range(int(s[0][0]), int(s[1][0])+1):
            for y in range(int(s[0][1]), int(s[1][1])+1):
                grid[x][y] = 1
    elif "toggle" in row:
        s = row[6:]
        s = s.split('through')
        s[0] = s[0].split(',')
        s[1] = s[1].split(',')
        for x in range(int(s[0][0]), int(s[1][0])+1):
            for y in range(int(s[0][1]), int(s[1][1])+1):
                grid[x][y] = not grid[x][y]
    elif "turn off" in row:
        s = row[9:]
        s = s.split('through')
        s[0] = s[0].split(',')
        s[1] = s[1].split(',')
        for x in range(int(s[0][0]), int(s[1][0])+1):
            for y in range(int(s[0][1]), int(s[1][1])+1):
                grid[x][y] = 0

print(sum([sum(row) for row in grid]))
