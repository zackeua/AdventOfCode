import sys
import itertools
from copy import deepcopy


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

def flodfill(grid, pipe):
    data = deepcopy(grid)
    to_consider = [(0,0), (0, len(data[0])-1), (len(data)-1, 0), (len(data)-1, len(data[0])-1)]


    filled = 0
    while to_consider != []:
        current = to_consider[0]
        to_consider = to_consider[1:]

        if current not in pipe:
            if data[current[0]][current[1]] != '*':
                if current[0]+1 < len(data):
                    to_consider.append((current[0]+1, current[1]))
                if current[0]-1 >= 0:
                    to_consider.append((current[0]-1, current[1]))
                if current[1]+1 < len(data[0]):
                    to_consider.append((current[0], current[1]+1))
                if current[1]-1 >= 0: 
                    to_consider.append((current[0], current[1]-1))

                data[current[0]][current[1]] = '*'
                filled += 1
    
    return data, filled


def expand_rows(grid, pipe):
    data = []

    new_pipe = set()
    for elem in pipe:
        new_pipe.add((elem[0], elem[1]*2))



    for i, row in enumerate(grid):
        line = []
        for j, (elem1, elem2) in enumerate(itertools.pairwise(row)):
            line.append(elem1)
            if (i, j) not in pipe or (i, j+1) not in pipe:
                line.append('.')
            elif grid[i][j] in '|7J' and grid[i][j+1] in '|LF':
                line.append('.')
            else:
                line.append('-')
                new_pipe.add((i, j*2+1))
        line.append(elem2)
        data.append(line)
    return data, new_pipe

def expand_cols(grid, pipe):
    
    data = []
    new_pipe = set()
    for elem in pipe:
        new_pipe.add((elem[0]*2, elem[1]))
    
    for i, (row1, row2) in enumerate(itertools.pairwise(grid)):
        data.append(row1)
        line = []
        for j, (elem1, elem2) in enumerate(zip(row1, row2)):
            if (i, j) not in pipe or (i+1, j) not in pipe:
                line.append('.')
            elif elem1 in '-LJ' and elem2 in '-F7':
                line.append('.')
            else:
                line.append('|')
                new_pipe.add((i*2+1, j))
        data.append(line)
    data.append(row2)
    return data, new_pipe

def expand(grid, pipe):
    return expand_cols(*expand_rows(grid, pipe))

def shrink(grid):
    data = []
    for row in grid[::2]:
        data.append(row[::2])
    return data

def count_inside(grid, pipe):
    total = 0
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if (i, j) not in pipe:
                if elem != '*':
                    total += 1
    return total

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
        data = ['+' + line.strip() + '+' for line in data]
        data = ['+'*len(data[0])] + data + ['+'*len(data[0])]
        
        data = [[elem for elem in line] for line in data]


        (start_row, start_col) = find_start(data)
        
        connected = connected_directions(data, start_row, start_col)
        
        current_1 = connected[0]
        current_2 = connected[1]
        previous_1 = (start_row, start_col)
        previous_2 = (start_row, start_col)

        part_of_pipe = set()

        part_of_pipe.add((start_row, start_col))
        part_of_pipe.add(current_1)
        part_of_pipe.add(current_2)



        total = 1
        while current_1 != current_2:
            
            tmp_1 = get_next_position(data, current_1, previous_1)
            tmp_2 = get_next_position(data, current_2, previous_2)
            current_1, previous_1 = tmp_1, current_1
            current_2, previous_2 = tmp_2, current_2
            part_of_pipe.add(current_1)
            part_of_pipe.add(current_2)

            total += 1

        expanded_data, expanded_pipe = expand(data, part_of_pipe)

        filled_data, filled_elements = flodfill(expanded_data, expanded_pipe)

        filled_shrink_data = shrink(filled_data)        

        answer = count_inside(filled_shrink_data, part_of_pipe)

        print(answer)

if __name__ == '__main__':
    main()