import sys

def is_touching(positions):
    return abs(positions['H'][0] - positions['T'][0]) < 2 and abs(positions['H'][1] - positions['T'][1]) < 2

def move(positions, direction):
    if direction == 'R':
        positions['H'] = (positions['H'][0] + 1, positions['H'][1])
        if not is_touching(positions): positions['T'] = (positions['H'][0] - 1, positions['H'][1])
    elif direction == 'L':
        positions['H'] = (positions['H'][0] - 1, positions['H'][1])
        if not is_touching(positions): positions['T'] = (positions['H'][0] + 1, positions['H'][1])
    elif direction == 'U':
        positions['H'] = (positions['H'][0], positions['H'][1] + 1)
        if not is_touching(positions): positions['T'] = (positions['H'][0], positions['H'][1] - 1)
    elif direction == 'D':
        positions['H'] = (positions['H'][0], positions['H'][1] - 1)
        if not is_touching(positions): positions['T'] = (positions['H'][0], positions['H'][1] + 1)
    else:
        assert(False)
    return positions

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        positions = {'H': (0,0), 'T': (0,0)}
        visited = set([(0, 0)])
        #print(visited)
        for line in data:
            direction, amount = line.split(' ')
            amount = int(amount)
            for _ in range(amount):
                positions = move(positions, direction)
                #print(positions['T'])
                visited.add(positions['T'])

        print(len(visited))
        #print(visited)

if __name__ == '__main__':
    main()
