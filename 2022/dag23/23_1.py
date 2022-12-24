import sys


def show_grid(elves, x_range, y_range):
    for y in range(y_range[0], y_range[1] + 1):
        for x in range(x_range[0], x_range[1] + 1):
            if (x, y) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def check_north(elf, elves):
    x_pos, y_pos = elf
    if (x_pos - 1 , y_pos - 1) not in elves and (x_pos , y_pos - 1) not in elves and (x_pos + 1, y_pos - 1) not in elves:
        return (x_pos, y_pos - 1)
    return None
   
def check_south(elf, elves):
    x_pos, y_pos = elf
    if (x_pos - 1 , y_pos + 1) not in elves and (x_pos , y_pos + 1) not in elves and (x_pos + 1, y_pos + 1) not in elves:
        return (x_pos, y_pos + 1)
    return None

def check_west(elf, elves):
    x_pos, y_pos = elf
    if (x_pos - 1 , y_pos - 1) not in elves and (x_pos - 1, y_pos) not in elves and (x_pos - 1, y_pos + 1) not in elves:
        return (x_pos - 1, y_pos)
    return None

def check_east(elf, elves):
    x_pos, y_pos = elf
    if (x_pos + 1 , y_pos - 1) not in elves and (x_pos + 1, y_pos) not in elves and (x_pos + 1, y_pos + 1) not in elves:
        return (x_pos + 1, y_pos)
    return None



def get_change(elf, elves, move_elf, iteration_number):

    change_function = {0: check_north, 1: check_south, 2: check_west, 3: check_east}

    if move_elf:
        return elf

    i = 0
    while i < 4:
        change = change_function[(i + iteration_number) % 4](elf, elves)
        if change is not None:
            return change
        i += 1
    return elf


def first_half(elves, iteration_number):

    proposed_positions = []

    for elf in elves:
        x_pos, y_pos = elf
        add_elf = True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x_pos + x, y_pos + y) in elves and (x_pos + x, y_pos + y) != elf:
                    add_elf = False
        
        proposed_positions.append(get_change(elf, elves, add_elf, iteration_number))
    
    return proposed_positions
    

def second_half(elves, proposed_positions, x_range, y_range):
    x_min, x_max = x_range
    y_min, y_max = y_range

    new_elves = []

    for elf, proposed in zip(elves, proposed_positions):
        if proposed_positions.count(proposed) == 1:
            new_elf_x = proposed[0]
            new_elf_y = proposed[1]
        else:
            new_elf_x = elf[0]
            new_elf_y = elf[1]

        if new_elf_x > x_max:
            x_max = new_elf_x
        if new_elf_x < x_min:
            x_min = new_elf_x
        if new_elf_y > y_max:
            y_max = new_elf_y
        if new_elf_y < y_min:
            y_min = new_elf_y
        new_elves.append((new_elf_x, new_elf_y))

    return new_elves, (x_min, x_max), (y_min, y_max)


def step(elves, x_range, y_range, iteration_number):
    

    proposed_positions = first_half(elves, iteration_number)

    return second_half(elves, proposed_positions, x_range, y_range)



def main():

    with open(sys.argv[1], 'r') as f:
        data = [row.replace('\n', '') for row in f.readlines()]

        elves = []

        x_min = 10000
        x_max = 0
        y_min = 10000
        y_max = 0

        for y, row in enumerate(data):
            for x, elem in enumerate(row):
                if elem == '#':
                    elves.append((x, y))
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y

        #show_grid(elves, (x_min, x_max), (y_min, y_max))

        for i in range(10):
            elves , (x_min, x_max), (y_min, y_max) = step(elves, (x_min, x_max), (y_min, y_max), i) 
    
        total_size = (y_max - y_min + 1) * (x_max - x_min + 1) - len(elves)

        print(total_size)


if __name__ == '__main__':
    main()