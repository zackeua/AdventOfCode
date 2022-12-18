import sys

debug = False

def debug_print(*s, **args):
    if debug:
        print(*s, **args)

def show_board(piece, occupied, max_height):
    if debug:
        for row_index in range(max_height + 5, -1, -1):
            for column_index in range(0, 9):
                if (column_index, row_index) in occupied:
                    print('#', end='')
                elif (column_index, row_index) in piece:
                    print('@', end='')
                elif row_index == 0 and column_index in [0, 8]:
                    print('+', end='')
                elif row_index == 0:
                    print('-', end='')
                elif column_index in [0, 8]:
                    print('|', end='')
                else:
                    print('.', end='')
            print()
        print()
        input()



def get_next_piece(max_height, shape):
    if shape == '-':
        return ((3, max_height+3), (4, max_height+3), (5, max_height+3), (6, max_height+3)), '+'
    elif shape == '+':
        return ((3, max_height+4), (4, max_height+3), (4, max_height+4), (4, max_height+5), (5, max_height+4)), '_|'
    elif shape == '_|':
        return ((3, max_height+3), (4, max_height+3), (5, max_height+3), (5, max_height+4), (5, max_height+5)), '|'
    elif shape == '|':
        return ((3, max_height+3), (3, max_height + 4), (3, max_height + 5), (3, max_height + 6)), '='
    elif shape == '=':
        return ((3, max_height+3), (3, max_height+4), (4, max_height+3), (4, max_height+4)), '-'
    else:
        assert(False, 'Should not reach this case')

def move_piece_horisontally(op, piece, occupied):
    
    update = lambda a: a + 1 if op == '>' else  a - 1

    next_piece = []
    for part in piece:
        new_part = (update(part[0]), part[1])
        next_piece.append(new_part)
        if new_part in occupied or not (0 < new_part[0] < 8): # TODO: only check the parts of the pieces that potentially can move into occupied locations
            if op == '>':
                debug_print('Jet of gas pushes rock right, but nothing happens:')
            else:
                debug_print('Jet of gas pushes rock left, but nothing happens:')
            return piece
    if op == '>':
        debug_print('Jet of gas pushes rock right:')
    else:
        debug_print('Jet of gas pushes rock left:')
    return tuple(next_piece)
        

def move_piece_down(piece, occupied):
    next_piece = []
    for part in piece:
        new_part = (part[0], part[1] - 1)
        next_piece.append(new_part)
        if new_part in occupied or new_part[1] < 1: # TODO: only check the parts of the pieces that potentially can move into occupied locations
            debug_print(f'Rock falls 1 unit, causing it to come to rest:')
            return piece, False
    debug_print(f'Rock falls 1 unit:')
    return tuple(next_piece), True

def add_to_occupied(piece, occupied, max_height):
    new_max_height = max_height
    for part in piece:
        if new_max_height < part[1]:
            new_max_height = part[1]
        occupied.add(part)
    return occupied, new_max_height


def run(ops):
    c = 0
    i = 0
    l = len(ops)
    max_height = 1
    occupied = set()
    shape = '-'
    piece, shape = get_next_piece(max_height, shape)
    while c < 2022:
        # do stuff here
        continue_move_piece = True
        while continue_move_piece:
            show_board(piece, occupied, max_height)
            piece = move_piece_horisontally(ops[i], piece, occupied)
            i = (i + 1) % l
            show_board(piece, occupied, max_height)
            piece, continue_move_piece = move_piece_down(piece, occupied)
        occupied, max_height = add_to_occupied(piece, occupied, max_height)
        c += 1
        piece, shape = get_next_piece(max_height+1, shape)
    print(max_height)

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readline().replace('\n', '')
        run(data)


if __name__ == '__main__':
    main()
