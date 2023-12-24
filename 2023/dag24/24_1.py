import sys


def sign(number):
    return number / abs(number)


def determinant(point1, point2):
    return point1[0] * point2[1] - point1[1] * point2[0]


def intersects(point1, direction1, point2, direction2):
    print(f'Hailstone A: {point2} @ {direction2}')
    print(f'Hailstone B: {point1} @ {direction1}')

    point1_start = point1
    point1_end = [point1[0] + direction1[0], point1[1] + direction1[1]]

    point2_start = point2
    point2_end = [point2[0] + direction2[0], point2[1] + direction2[1]]

    d_1 = determinant(point1_start, point1_end)
    d_x1 = determinant((point1_start[0], point1_end[0]), (1, 1))
    d_y1 = determinant((point1_start[1], point1_end[1]), (1, 1))

    d_2 = determinant(point2_start, point2_end)
    d_x2 = determinant((point2_start[0], point2_end[0]), (1, 1))
    d_y2 = determinant((point2_start[1], point2_end[1]), (1, 1))

    x_numerator = determinant((d_1, d_2), (d_x1, d_x2))
    y_numerator = determinant((d_1, d_2), (d_y1, d_y2))

    denomenator = determinant((d_x1, d_x2), (d_y1, d_y2))

    if denomenator == 0:
        return False, None, None

    x_intersect = x_numerator / denomenator
    y_intersect = y_numerator / denomenator

    lower_bound = 7
    upper_bound = 27

    lower_bound = 200000000000000
    upper_bound = 400000000000000

    sign_1_condition = sign(x_intersect - point1_start[0]) == sign(direction1[0]) and \
        sign(y_intersect - point1_start[1]) == sign(direction1[1])

    sign_2_condition = sign(x_intersect - point2_start[0]) == sign(direction2[0]) and \
        sign(y_intersect - point2_start[1]) == sign(direction2[1])

    if lower_bound <= x_intersect <= upper_bound and lower_bound <= y_intersect <= upper_bound:
        if sign_1_condition and sign_2_condition:
            # print(f'Hailstones\' paths will cross inside the test area (at x={
            #       x_intersect:.3f}, y={y_intersect:.3f}).')
            return True, x_intersect, y_intersect
        elif not sign_1_condition and not sign_2_condition:
            pass
            # print('Crossed in the past for both hailstones')
        elif not sign_1_condition:
            pass
            # print('Crossed in the past for hailstone A')
        elif not sign_2_condition:
            pass
            # print('Crossed in the past for hailstone B')
    else:
        pass
        # print(f'Crossing outside of test area(at x={
        #     x_intersect:.3f}, y={y_intersect:.3f}).')

    return False, x_intersect, y_intersect


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[list(map(int, elem.split(',')))
                 for elem in line.strip().split(' @ ')] for line in data]
        total = 0
        for i, (point, direction) in enumerate(data):
            for j in range(i):
                point2, direction2 = data[j]
                valid, x, y = intersects(point, direction, point2, direction2)
                print()
                if valid:
                    total += 1
        print(total)
        assert total < 29320


if __name__ == '__main__':
    main()
