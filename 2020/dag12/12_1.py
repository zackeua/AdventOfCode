import sys
with open(sys.argv[1], 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = data[:-1]

facing = "east"

d = {'east': {'L90':'north', 'L180': 'west', 'L270':'south', 'R90':'south', 'R180':'west', 'R270':'north'},
      'north': {'L90':'west', 'L180': 'south', 'L270': 'east', 'R90':'east', 'R180':'south', 'R270':'west'},
      'west': {'L90':'south', 'L180': 'east', 'L270': 'north', 'R90':'north', 'R180':'east', 'R270':'south'},
      'south': {'L90':'east', 'L180': 'north', 'L270': 'west', 'R90':'west', 'R180':'north', 'R270':'east'}}
dirs = {'east':0, 'north':0, 'south':0, 'west':0}

for dir in data:
    if dir[0] == "L" or dir[0] == "R":
        facing = d[facing][dir]
    if dir[0] == "F":
        dirs[facing] += int(dir[1:])
    if dir[0] == "N":
        dirs['north'] += int(dir[1:])
    if dir[0] == "S":
        dirs['south'] += int(dir[1:])
    if dir[0] == "E":
        dirs['east'] += int(dir[1:])
    if dir[0] == "W":
        dirs['west'] += int(dir[1:])

print(abs(dirs['north']-dirs['south'])+abs(dirs['east']-dirs['west']))
