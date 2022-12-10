import sys
debug = False

def debug_print(*s, **args):
    if debug:
        print(*s, **args)

def if_print_pixel(cycle, register, grid):
    debug_print(f'During cycle  {cycle}: CRT draws pixel in position {cycle - 1}')
    char_to_print = '#' if max([(register['X'] - 1), 0]) % 40 <= (cycle-1) % 40 <= min([(register['X'] + 1), 39]) % 40 else '.'
    grid += char_to_print
    if cycle%40 ==0:
        grid += '\n                 '
    debug_print(f'Current CRT row: {grid}')
    return grid

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.replace('\n', '') for line in data]
        register = {'X': 1}
        result = 0
        cycle = 0
        grid = ''
        for _, line in enumerate(data):
            #if cycle > 38:
            #    sys.exit()
            cycle += 1
            sprite_position = ''.join(['#' if max([(register['X'] - 1), 0]) % 40 <= i % 40 <= min([(register['X'] + 1), 39]) % 40 else '.' for i in range(40)])
            debug_print(f'Sprite position: {sprite_position}')
            debug_print()
            debug_print(f'Start cycle   {cycle}: begin executing {line}')
            grid = if_print_pixel(cycle, register, grid)
            if 'addx' in line:
                _, amount = line.split()
                
                cycle += 1
                grid = if_print_pixel(cycle, register, grid)
                register['X'] += int(amount)

            else:
                pass
            x_value = f'(Register X is now {register["X"]})'
            debug_print(f'End of cycle {cycle}: finish executing {line} {x_value if "addx" in line else ""}')
        
        print('                 ' + grid)

if __name__ == '__main__':
    main()
