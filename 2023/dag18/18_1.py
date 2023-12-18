import sys
import itertools

def dig(data):

    current = (0, 0)
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    boundary = []
    corners = []
    for direction, length, _ in data:
        for i in range(int(length)):
            if direction == 'R':
                current = (current[0] + 1, current[1])
            elif direction == 'L':
                current = (current[0] - 1, current[1])
            elif direction == 'U':
                current = (current[0], current[1] + 1)
            elif direction == 'D':
                current = (current[0], current[1] - 1)

            if current[0] < min_x:
                min_x = current[0]
            elif current[0] > max_x:
                max_x = current[0]
            elif current[1] < min_y:
                min_y = current[1]
            elif current[1] > max_y:
                max_y = current[1]
            boundary.append(current)
        corners.append(current)

    return boundary, min_x-1, max_x+1, min_y-1, max_y+1, corners

def draw(boundary, min_x, max_x, min_y, max_y):
    for y in range(max_y-1, min_y-1+1, -1):
        for x in range(min_x+1, max_x+1-1):
            if (x, y) in boundary:
                print('#', end='')
            else:
                print('.', end='')
        print()


def calculate_area(boundary, min_x, max_x, min_y, max_y):
    area = 0
    for y in range(max_y-1, min_y-1+1, -1):
        x_min_edge = min_x
        while (x_min_edge, y) not in boundary:
            x_min_edge += 1
        x_max_edge = max_x
        while (x_max_edge, y) not in boundary:
            x_max_edge -= 1
        area += x_max_edge - x_min_edge + 1 
    return area
    # shoe lace formula
    area = 0
    for p1, p2 in itertools.pairwise(boundary):
        area += p1[0] * p2[1] - p2[0] * p1[1]
    area += boundary[-1][0] * boundary[0][1] - boundary[0][0] * boundary[-1][1]
    return abs(area) // 2


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [line.split(' ') for line in data]
        
        info = dig(data)
        
        # draw(info[0], info[1], info[2], info[3], info[4])
        area = calculate_area(info[0], info[1], info[2], info[3], info[4])

        print(area)
        
if __name__ == '__main__':
    main()
