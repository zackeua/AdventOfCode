import sys
import re


def visualise(points, right, bottom):
    counts = {}
    for point in points:
        if point not in counts:
            counts[point] = 0
        counts[point] += 1

    for y in range(bottom):
        for x in range(right):
            if (x, y) not in counts:
                print('.', end='')
            else:
                print(counts[(x, y)], end='')
        print()


def visualise_quadrants(points, right, bottom):
    counts = {}
    for point in points:
        if point not in counts:
            counts[point] = 0
        counts[point] += 1
    x_center = (right) // 2
    y_center = (bottom) // 2

    for y in range(bottom):
        if y == y_center:
            print()
            continue
        for x in range(right):
            if x == x_center:
                print(' ', end='')
            elif (x, y) not in counts:
                print('.', end='')
            else:
                print(counts[(x, y)], end='')
        print()


def step(point_vel, right, bottom, steps):
    points = []
    for i, (point, velocity) in enumerate(point_vel):
        new_point_x = (point[0] + velocity[0] * steps) % (right)
        new_point_y = (point[1] + velocity[1] * steps) % (bottom)
        points.append((new_point_x, new_point_y))
    return points


def calculate_security_score(points, right, bottom):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    x_center = (right) // 2
    y_center = (bottom) // 2
    for point in points:
        if point[0] < x_center and point[1] < y_center:
            q1 += 1
        elif point[0] < x_center and y_center < point[1]:
            q2 += 1
        elif x_center < point[0] and point[1] < y_center:
            q3 += 1
        elif x_center < point[0] and y_center < point[1]:
            q4 += 1

    return q1 * q2 * q3 * q4


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
    regex = re.compile(r'p=(-{0,1}\d+),(-{0,1}\d+) v=(-{0,1}\d+),(-{0,1}\d+)')

    right = 11  # 101
    bottom = 7  # 103
    right = 101
    bottom = 103
    steps = 100

    point_vel = []
    for line in data:
        matches = regex.findall(line)
        point = (int(matches[0][0]), int(matches[0][1]))
        velocity = (int(matches[0][2]), int(matches[0][3]))
        point_vel.append((point, velocity))

    points = step(point_vel, right, bottom, steps)

    # visualise(points, right, bottom)
    # print()
    # print()

    # visualise_quadrants(points, right, bottom)

    result = calculate_security_score(points, right, bottom)
    print(result)
    assert result != 221579072


if __name__ == '__main__':
    main()
