import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [[int(elem) for elem in row if elem != '\n'] for row in data]


totsum = 0
sizes = []
visited = [[False for _ in row] for row in data]

for i in range(len(data)):
    for j in range(len(data[0])):
        nextPt = []
        if not visited[i][j] and data[i][j] != 9:
            nextPt.append((i,j))

        current = 0
        
        while len(nextPt) != 0:
            visited[nextPt[0][0]][nextPt[0][1]] = True
            current += 1

            if nextPt[0][0] != 0:
                if not visited[nextPt[0][0]-1][nextPt[0][1]] and data[nextPt[0][0]-1][nextPt[0][1]] != 9:
                    pt = (nextPt[0][0]-1, nextPt[0][1])
                    if pt not in nextPt: nextPt.append(pt)

            if nextPt[0][0] != len(data) - 1:
                if not visited[nextPt[0][0]+1][nextPt[0][1]] and data[nextPt[0][0]+1][nextPt[0][1]] != 9:
                    pt = (nextPt[0][0]+1, nextPt[0][1])
                    if pt not in nextPt:
                        nextPt.append(pt)

            if nextPt[0][1] != 0:
                if not visited[nextPt[0][0]][nextPt[0][1]-1] and data[nextPt[0][0]][nextPt[0][1]-1] != 9:
                    pt = (nextPt[0][0], nextPt[0][1]-1)
                    if pt not in nextPt: nextPt.append(pt)

            if nextPt[0][1] != len(data[0]) - 1:
                if not visited[nextPt[0][0]][nextPt[0][1]+1] and data[nextPt[0][0]][nextPt[0][1]+1] != 9:
                    pt = (nextPt[0][0], nextPt[0][1]+1)
                    if pt not in nextPt:
                        nextPt.append(pt)

            
            nextPt = nextPt[1:]
        sizes += [current]
        sizes.sort()
        sizes = sizes[-3:]

print(sizes[0] * sizes[1] * sizes[2])
