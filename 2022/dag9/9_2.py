import sys


def is_touching(positions, elem1, elem2):
    return abs(positions[elem1][0] - positions[elem2][0]) < 2 and abs(positions[elem1][1] - positions[elem2][1]) < 2

def get_direction(positions, elem, prev):
    if positions[elem][0] < prev[0] and positions[elem][1] == prev[1]:
        return 'R'
    elif positions[elem][0] < prev[0] and positions[elem][1] < prev[1]:
        return 'RU'
    elif positions[elem][0] < prev[0] and positions[elem][1] > prev[1]:
        return 'RD'
    elif positions[elem][0] > prev[0] and positions[elem][1] == prev[1]:
        return 'L'
    elif positions[elem][0] > prev[0] and positions[elem][1] < prev[1]:
        return 'LU'
    elif positions[elem][0] > prev[0] and positions[elem][1] > prev[1]:
        return 'LD'
    elif positions[elem][1] < prev[1]:
        return 'U'
    elif positions[elem][1] > prev[1]:
        return 'D'
    else:
        return None
    

def next_elem(elem):
    if elem == 'H':
        return '1'
    if elem == '9':
        return None
    
    return chr(ord(elem) + 1)

def move(positions, direction, elem):
    if direction is None:
        return positions

    if elem is None:
        return positions

    previous = positions[elem]
    next_element = next_elem(elem)

    if direction == 'R':
        positions[elem] = (positions[elem][0] + 1, positions[elem][1])
    elif direction == 'L':
        positions[elem] = (positions[elem][0] - 1, positions[elem][1])
    elif direction == 'U':
        positions[elem] = (positions[elem][0], positions[elem][1] + 1)
    elif direction == 'D' :
        positions[elem] = (positions[elem][0], positions[elem][1] - 1)
    elif direction == 'RU':
        positions[elem] = (positions[elem][0] + 1, positions[elem][1] + 1)
    elif direction == 'RD':
        positions[elem] = (positions[elem][0] + 1, positions[elem][1] - 1)
    elif direction == 'LU':
        positions[elem] = (positions[elem][0] - 1, positions[elem][1] + 1)
    elif direction == 'RD':
        positions[elem] = (positions[elem][0] - 1, positions[elem][1] - 1)

    if next_element is not None:
        if not is_touching(positions, elem, next_element):
            direction = get_direction(positions, next_element, previous)
            positions = move(positions, direction, next_element)
       

    return positions

def show_grid(positions, min, max):
    grid = {(i, j):'.' for i in range(min, max) for j in range(min, max)}
    grid[(0, 0)] = 's'
    grid[positions['9']] = '9'
    grid[positions['8']] = '8'
    grid[positions['7']] = '7'
    grid[positions['6']] = '6'
    grid[positions['5']] = '5'
    grid[positions['4']] = '4'
    grid[positions['3']] = '3'
    grid[positions['2']] = '2'
    grid[positions['1']] = '1'
    grid[positions['H']] = 'H'
    print(positions['1'])
    for j in range(max-1, min-1, -1):
        for i in range(min, max):
            print(grid[(i, j)], end='')
        print()

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        positions = {'H': (0, 0), '1': (0, 0), '2': (0, 0), '3': (0,0), '4': (0,0), '5': (0,0), '6':(0,0), '7': (0,0), '8': (0,0), '9': (0,0)}
        visited = set([(0, 0)])
        #print(visited)
        for line in data:
            direction, amount = line.split(' ')
            amount = int(amount)
            for _ in range(amount):
                positions = move(positions, direction, 'H')
                visited.add(positions['9'])
                #print(positions['9'])
                #show_grid(positions, 0, 6)
            show_grid(positions, -11, 14)
            input()

        print(len(visited))
        print(visited)


if __name__ == '__main__':
    main()
