import sys


def find_stones(data):

    stones = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                stones.add((i, j))
    return stones


def get_starting_point(data):

    position = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                position.add((i, j))
                return position


def step(data, stones, positions, width, height):

    new_positions = set()
    for position in positions:
        if (position[0] % height, (position[1]+1) % width) not in stones:
            new_positions.add((position[0], position[1]+1))

        if ((position[0]+1) % height, position[1] % width) not in stones:
            new_positions.add((position[0]+1, position[1]))

        if (position[0] % height, (position[1]-1) % width) not in stones:
            new_positions.add((position[0], position[1]-1))

        if ((position[0]-1) % height, position[1] % width) not in stones:
            new_positions.add((position[0]-1, position[1]))

    return new_positions


def show(data, positions):

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if (i, j) in positions:
                print('O', end='')
            else:
                print(char, end='')
        print()


def get_result(number, gain_rate, starting_point, starting_value, second_point, second_value, step_length):

    ans = {starting_point: starting_value, second_point: second_value}

    for i in range(starting_point, number+(2*step_length), step_length):
        ans[i+2*step_length] = ans[i+step_length] * 2 - ans[i] + gain_rate
    return ans[number]
    '''
    gain = ans[i] - ans[i-1]
    previous_gain = ans[i-1] - ans[i-2]
    
    ans[i] = ans[i-1] + gain
    ans[i-1] = ans[i-2] + previous_gain

    gain_rate = ans[i] - 2 * ans[i-1] + ans[i-2]

    ans[i] = ans[i-1 *2 - and[i-2] + gain_rate

    '''


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        stones = find_stones(data)
        points = get_starting_point(data)
        width = len(data[0])
        height = len(data)
        steps = 26501365
        total = 0
        # print(f'{width = }, {height = }')
        previous_number_of_points = 0
        previous_gain = 0
        previous_gain_rate = 0
        can_break = False
        wait_one_more = False
        break_point = 0
        break_value = 0
        for i in range(1, steps+1):
            points = step(data, stones, points, width, height)
            # if i in [6, 10, 50, 100]:
            #    print(f'After {i} steps: {len(points)}')
            #    print()

            if i % (width) == 0:
                gain = len(points) - previous_number_of_points
                gain_rate = gain - previous_gain
                print(i, len(points), gain, gain_rate)
                if gain_rate == previous_gain_rate:
                    can_break = True
                previous_number_of_points = len(points)
                previous_gain = gain
                previous_gain_rate = gain_rate

            if can_break and i % width == steps % width:
                if wait_one_more:
                    break
                break_point = i
                break_value = len(points)
                wait_one_more = True

        ans = get_result(steps, gain_rate, break_point, break_value, i, len(points), width)
        print(ans)
        # 5000 ans gain gain_rate
        # print(gain_rate ** ((steps-i-2) % width) + len(points))
        # print(len(points))


if __name__ == '__main__':
    main()
