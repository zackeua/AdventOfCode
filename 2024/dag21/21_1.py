import sys

NUMPAD_PRESSES = {'7': {'7': 'A', '8': '>A', '9': '>>A',
                        '4': 'vA', '5': '>vA', '6': '>>vA',
                        '1': 'vvA', '2': '>vvA', '3': '>>vvA',
                        '0': '>vvvA', 'A': '>>vvvA'},
                  '8': {'7': '<A', '8': 'A', '9': '>A',
                        '4': '<vA', '5': 'vA', '6': '<>vA',
                        '1': '<vA', '2': 'vvA', '3': '<>vvA',
                        '0': 'vvvA', 'A': '>vvvA'},
                  '9': {'7': '<<A', '8': '<A', '9': 'A',
                        '4': '<<vA', '5': '<vA', '6': '<<vA',
                        '1': '<<vA', '2': '<vvA', '3': '<<vvA',
                        '0': '<vvvA', 'A': 'vvvA'},

                  '4': {'7': '^A', '8': '>^A', '9': '>>^A',
                        '4': 'A', '5': '>A', '6': '>>A',
                        '1': 'vA', '2': '>vA', '3': '>>vA',
                        '0': '>vvA', 'A': '>>vvA'},
                  '5': {'7': '<^A', '8': '^A', '9': '>^A',
                        '4': '<A', '5': 'A', '6': '>A',
                        '1': 'v<A', '2': 'vA', '3': '>vA',
                        '0': 'vvA', 'A': '>vvA'},
                  '6': {'7': '<<^A', '8': '<^A', '9': '^A',
                        '4': '<<A', '5': '<A', '6': 'A',
                        '1': 'v<<A', '2': 'v<A', '3': 'vA',
                        '0': '<vvA', 'A': 'vvA'},

                  '1': {'7': '^^A', '8': '>^^A', '9': '>>^^A',
                        '4': '^A', '5': '>^A', '6': '>>^A',
                        '1': 'A', '2': '>A', '3': '>>A',
                        '0': '>vA', 'A': '>>vA'},
                  '2': {'7': '^^<A', '8': '^^A', '9': '>^^A',
                        '4': '^<A', '5': '^A', '6': '>^A',
                        '1': '<A', '2': 'A', '3': '>A',
                        '0': 'vA', 'A': '>vA'},
                  '3': {'7': '^^<<A', '8': '^^<A', '9': '^^A',
                        '4': '^<<A', '5': '^<A', '6': '^A',
                        '1': '<<A', '2': '<A', '3': 'A',
                        '0': 'v<A', 'A': 'vA'},

                  '0': {'7': '^^^<A', '8': '^^^A', '9': '>^^^A',
                        '4': '^^<A', '5': '^^A', '6': '>^^A',
                        '1': '^<A', '2': '^A', '3': '^>A',
                        '0': 'A', 'A': '>A'},
                  'A': {'7': '^^^<<A', '8': '^^^<A', '9': '^^^A',
                        '4': '^^<<A', '5': '^^<A', '6': '^^A',
                        '1': '^<<A', '2': '^<A', '3': '^A',
                        '0': '<A', 'A': 'A'}
                  }

KEYPAD_PRESSES = {'^': {'^': 'A', 'A': '>A',
                        '<': 'v<A', 'v': 'vA', '>': 'v>A'},
                  'A': {'^': '<A', 'A': 'A',
                        '<': 'v<<A', 'v': '<vA', '>': 'vA'},

                  '<': {'^': '>^A', 'A': '>>^A',
                        '<': 'A', 'v': '>A', '>': '>>A'},
                  'v': {'^': '^A', 'A': '>^A',
                        '<': '<A', 'v': 'A', '>': '>A'},
                  '>': {'^': '<^A', 'A': '^A',
                        '<': '<<A', 'v': '<A', '>': 'A'}

                  }


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        print(data)

    robot_1_position = 'A'
    robot_2_position = 'A'
    robot_3_position = 'A'

    total = 0
    for sequence in data:
        print(sequence)
        robot_1_movements = ''
        robot_2_movements = ''
        robot_3_movements = ''
        for key_1 in sequence:
            robot_1_movement = NUMPAD_PRESSES[robot_1_position][key_1]
            robot_1_position = key_1
            robot_1_movements += robot_1_movement
            for key_2 in robot_1_movement:
                robot_2_movement = KEYPAD_PRESSES[robot_2_position][key_2]
                robot_2_position = key_2
                robot_2_movements += robot_2_movement
                for key_3 in robot_2_movement:
                    robot_3_movement = KEYPAD_PRESSES[robot_3_position][key_3]
                    robot_3_position = key_3
                    robot_3_movements += robot_3_movement

        print(robot_3_movements)
        print(robot_2_movements)
        print(robot_1_movements)
        print(len(robot_3_movements), ' * ', int(sequence[:-1]))
        print(len(robot_3_movements) * int(sequence[:-1]))
        total += len(robot_3_movements) * int(sequence[:-1])
    print(total)


if __name__ == '__main__':
    main()
