import sys
def rot(deg,waypoint):
    if deg in ['L90', 'R270']:
        waypoint = [waypoint[1], -waypoint[0]]
    if deg in ['L180', 'R180']:
        waypoint = [-waypoint[0], -waypoint[1]]
    if deg in ['L270', 'R90']:
        waypoint = [-waypoint[1], waypoint[0]]
    return waypoint


with open(sys.argv[1], 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = data[:-1]


position = [0, 0]
waypoint = [1,10]

for dir in data:
    if dir[0] in ['L', 'R']:
        waypoint = rot(dir,waypoint)
    if dir[0] == "F":
        times = int(dir[1:])
        position[0] += waypoint[0]*times
        position[1] += waypoint[1]*times
    if dir[0] == "N":
        waypoint[0] += int(dir[1:])
    if dir[0] == "S":
        waypoint[0] -= int(dir[1:])
    if dir[0] == "E":
        waypoint[1] += int(dir[1:])
    if dir[0] == "W":
        waypoint[1] -= int(dir[1:])

print(abs(position[0])+abs(position[1]))
