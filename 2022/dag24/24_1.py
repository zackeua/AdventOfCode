import sys
import heapq


def show_grid(state, target, blizzard_list, x_size, y_size):
    timepoint, player_position_x, player_position_y = state

    new_blizzards = tuple([update_blizzard(blizzard, timepoint, x_size, y_size)[1:] for blizzard in blizzard_list]) 
    #print(new_blizzards)

    print(player_position_x, player_position_y, x_size, y_size)
    for x in range(x_size + 2):
        if x == 1:
            print('.', end='')
        else:
            print('#', end='')
    print()
    for y in range(y_size):
        print('#', end='')
        for x in range(x_size):
            c = new_blizzards.count((x, y))
            if (x, y) == state[1:]:
                print('E', end='')
            elif (x, y) == target[1:]:
                print('T', end='')
            elif c > 0:
                print(c, end='')
            else:
                print('.', end='')
        print('#')

    for x in range(x_size + 2):
        if x == x_size:
            print('.', end='')
        else:
            print('#', end='')
        

def update_blizzard(blizzard, timepoint, x_size, y_size):
    if blizzard[0] == '<':
        return (timepoint, (blizzard[1] - timepoint) % x_size, blizzard[2] % y_size)
    elif blizzard[0] == '>':
        return (timepoint, (blizzard[1] + timepoint) % x_size, blizzard[2] % y_size)
    elif blizzard[0] == 'v':
        return (timepoint, blizzard[1] % x_size , (blizzard[2] + timepoint) % y_size)
    elif blizzard[0] == '^':
        return (timepoint, blizzard[1] % x_size, (blizzard[2] - timepoint) % y_size)
    else:
        assert(False, 'Should not reach this state')


def possible_moves(state, blizzard_list, x_size, y_size):
    #print(state)
    timepoint, player_position_x, player_position_y = state
    new_blizzards = tuple([update_blizzard(blizzard, timepoint + 1, x_size, y_size) for blizzard in blizzard_list]) 

    #print(state)
    #print(new_blizzards)


    possible_positions = [(timepoint + 1, player_position_x, player_position_y),
                          (timepoint + 1, player_position_x + 1, player_position_y),
                          (timepoint + 1, player_position_x - 1, player_position_y),
                          (timepoint + 1, player_position_x, player_position_y + 1),
                          (timepoint + 1, player_position_x, player_position_y - 1)]

    possible_positions = [position for position in possible_positions if 0 <= position[1] < x_size and 0 <= position[2] < y_size]
    #print([position for position in possible_positions if position not in new_blizzards])
    return tuple([position for position in possible_positions if position not in new_blizzards])


def dijkstras(heap: heapq, target, blizzard_list, x_size, y_size) -> int:
    visited = set()
    while heap != []:
        u = heapq.heappop(heap)
        #print(heap)
        #input()
        #print(u, target)
        if (u[1], u[2]) == target: # found target node
            return u[0]

        visited.add(u)
        #show_grid(u, target, blizzard_list, x_size, y_size)
        #input()
        new_moves = possible_moves(u, blizzard_list, x_size, y_size)

        for move in new_moves:
            if move not in visited and move not in heap:
                heapq.heappush(heap, move)


def main():
    
    with open(sys.argv[1], 'r') as f:
        data = [row.replace('\n', '') for row in f.readlines()]
        

        blizzard_list = []

        y_size = len(data[1:-1])
        x_size = len(data[1][1:-1])
        for y, row in enumerate(data[1:-1]):
            for x, elem in enumerate(row[1:-1]):
                if elem != '.':
                    blizzard_list.append((elem, x, y))


        start_position = [(1, 0, 0)]
        #print(blizzard_list)
        heapq.heapify(start_position)

        time = dijkstras(start_position, (x_size - 1, y_size - 1), blizzard_list, x_size, y_size)

        #print(data)
        print(time + 1)

if __name__ == '__main__':
    main()
