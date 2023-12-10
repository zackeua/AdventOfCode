import sys

def find_start(data):
    for row, line in enumerate(data):
        for col, elem in enumerate(line):
            if elem == 'S':
                return (row, col)


def connected_directions(data, row, col):
    pipes = []

    if data[row-1][col] in '|F7':
        pipes.append((row-1, col))
    if data[row][col-1] in '-FL':
        pipes.append((row, col-1))
    if data[row][col+1] in '-7J':
        pipes.append((row, col+1))
    if data[row+1][col] in '|JL':
        pipes.append((row+1, col))

    return pipes

def get_next_position(data, current, previous):

    element = data[current[0]][current[1]]
    if element == '-':
        next_pos = (current[0], current[1]-1)
        return next_pos if next_pos != previous else (current[0], current[1]+1)
    elif element == '|':
        next_pos = (current[0]-1, current[1])
        return next_pos if next_pos != previous else (current[0]+1, current[1])
    elif element == 'F':
        next_pos = (current[0], current[1]+1)
        return next_pos if next_pos != previous else (current[0]+1, current[1])
    elif element == '7':
        next_pos = (current[0], current[1]-1)
        return next_pos if next_pos != previous else (current[0]+1, current[1])
    elif element == 'J':
        next_pos = (current[0], current[1]-1)
        return next_pos if next_pos != previous else (current[0]-1, current[1])
    elif element == 'L':
        next_pos = (current[0], current[1]+1)
        return next_pos if next_pos != previous else (current[0]-1, current[1])
    assert False # should not reach this



def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = ['.' + line.strip() + '.' for line in data]
        data = ['+'*len(data[0])] + data + ['.'*len(data[0])]
        
        (start_row, start_col) = find_start(data)

        connected = connected_directions(data, start_row, start_col)
        
        current_1 = connected[0]
        current_2 = connected[1]
        previous_1 = (start_row, start_col)
        previous_2 = (start_row, start_col)

        total = 1
        while current_1 != current_2:
            
            tmp_1 = get_next_position(data, current_1, previous_1)
            tmp_2 = get_next_position(data, current_2, previous_2)
            current_1, previous_1 = tmp_1, current_1
            current_2, previous_2 = tmp_2, current_2

            total += 1

        print(total)


if __name__ == '__main__':
    main()