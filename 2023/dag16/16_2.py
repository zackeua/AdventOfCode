import sys


def print_grid(grid, energized_positions):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in energized_positions:
                print('#', end='')
            else:
                print(grid[y][x], end='')
        print()
    print()


def send_ray(x, y, dx, dy, grid, energized_positions):
    rays = [(x, y, dx, dy)]
    sent_rays = set()
    while rays != []:
        ray = rays.pop()
        if ray in sent_rays:
            continue
        sent_rays.add(ray)
        x = ray[0]
        y = ray[1]
        dx = ray[2]
        dy = ray[3]

        while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
            energized_positions.add((x, y))
            if grid[y][x] == '.':
                pass
            elif grid[y][x] == '/':
                if dx == 1:
                    dx = 0
                    dy = -1
                elif dx == -1:
                    dx = 0
                    dy = 1
                elif dy == 1:
                    dx = -1
                    dy = 0
                elif dy == -1:
                    dx = 1
                    dy = 0
            elif grid[y][x] == '\\':
                if dx == 1:
                    dx = 0
                    dy = 1
                elif dx == -1:
                    dx = 0
                    dy = -1
                elif dy == 1:
                    dx = 1
                    dy = 0
                elif dy == -1:
                    dx = -1
                    dy = 0
            elif grid[y][x] == '|':
                if dx != 0:
                    rays.append((x, y, 0, 1))
                    rays.append((x, y, 0, -1))
                    break
            elif grid[y][x] == '-':
                if dy != 0:
                    rays.append((x, y, 1, 0))
                    rays.append((x, y, -1, 0))
                    break
            x += dx
            y += dy
            # print_grid(grid, energized_positions)
            # input()
    return energized_positions

def get_start_position(grid):
    for y in range(len(grid)):
       yield (0, y, 1, 0)
       yield (len(grid[0]) - 1, y, -1, 0)
    for x in range(len(grid[0])):
        yield (x, 0, 0, 1)
        yield (x, len(grid) - 1, 0, -1)


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        maximum = 0
        for start in get_start_position(data):
            energized_positions = set()
            energized_positions = send_ray(*start, data, energized_positions)
            maximum = max(maximum, len(energized_positions))
       
        
        print(maximum)

if __name__ == '__main__':
    main()

