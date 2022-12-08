import sys
import functools

def get_neighbours(position):
    x, y = position
    return ((x, y-1), (x-1, y), (x+1, y), (x, y+1))

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [row.replace('\n', '') for row in data]
        data = [list(map(int, row)) for row in data]
        is_visible = [[-1 for _ in row] for row in data]
        for i, _ in enumerate(data):
            is_visible[i][0] = 1
            is_visible[i][len(data[0])-1] = 1
        for i, _ in enumerate(data[0]):
            is_visible[0][i] = 1
            is_visible[len(data)-1][i] = 1
        
        nested_elems_to_updata = [[(i, j) for j, elem in enumerate(row) if elem == -1] for i, row in enumerate(is_visible)]
        elems_to_update = functools.reduce(lambda a, b: a + b, nested_elems_to_updata)

        while elems_to_update != []:
            current_element = elems_to_update[0]
            elems_to_update = elems_to_update[1:]

            left_neighbours = data[current_element[0]][1:current_element[1]+1]
            right_neighbours = data[current_element[0]][current_element[1]:-1]

            up_neighbors = [data[i][current_element[1]] for i, _ in enumerate(data)]
            down_neighbors = up_neighbors[current_element[0]:-1].copy()
            up_neighbors = up_neighbors[1:current_element[0]+1]

            if 0 not in [data[current_element[0]][current_element[1]] > data[current_element[0]][i-1] for i , _ in enumerate(left_neighbours, 1)] or \
               0 not in [data[current_element[0]][current_element[1]] > data[current_element[0]][i+1] for i , _ in enumerate(right_neighbours, current_element[1])] or \
               0 not in [data[current_element[0]][current_element[1]] > data[i-1][current_element[1]] for i , _ in enumerate(up_neighbors, 1)] or \
               0 not in [data[current_element[0]][current_element[1]] > data[i+1][current_element[1]] for i, _ in enumerate(down_neighbors, current_element[0])]:
               is_visible[current_element[0]][current_element[1]] = 1
            else:
               is_visible[current_element[0]][current_element[1]] = 0

        print(sum([sum(row) for row in is_visible]))
if __name__ == '__main__':
    main()
