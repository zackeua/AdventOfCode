import sys

NUMPAD_PRESSES = {'7': {'7': ['A'], '8': ['>A'], '9': ['>>A'],
                        '4': ['vA'], '5': ['>vA', 'v>A'], '6': ['>>vA', 'v>>A'],
                        '1': ['vvA'], '2': ['>vvA', 'vv>A'], '3': ['>>vvA', 'vv>>A'],
                        '0': ['>vvvA'], 'A': ['>>vvvA']},
                  '8': {'7': ['<A'], '8': ['A'], '9': ['>A'],
                        '4': ['<vA', 'v<A'], '5': ['vA'], '6': ['>vA', 'v>A'],
                        '1': ['<vvA', 'vv<A'], '2': ['vvA'], '3': ['>vvA', 'vv>A'],
                        '0': ['vvvA'], 'A': ['>vvvA', 'vvv>A']},
                  '9': {'7': ['<<A'], '8': ['<A'], '9': ['A'],
                        '4': ['<<vA', 'v<<A'], '5': ['<vA', 'v<A'], '6': ['vA'],
                        '1': ['<<vvA', 'vv<<A'], '2': ['<vvA', 'vv<A'], '3': ['vvA'],
                        '0': ['<vvvA', 'vvv<A'], 'A': ['vvvA']},

                  '4': {'7': ['^A'], '8': ['>^A', '^>A'], '9': ['>>^A', '^>>A'],
                        '4': ['A'], '5': ['>A'], '6': ['>>A'],
                        '1': ['vA'], '2': ['>vA', 'v>A'], '3': ['>>vA', 'v>>A'],
                        '0': ['>vvA'], 'A': ['>>vvA']},
                  '5': {'7': ['<^A', '^<A'], '8': ['^A'], '9': ['>^A', '^>A'],
                        '4': ['<A'], '5': ['A'], '6': ['>A'],
                        '1': ['v<A', '<vA'], '2': ['vA'], '3': ['>vA', 'v>A'],
                        '0': ['vvA'], 'A': ['>vvA', 'vv>A']},
                  '6': {'7': ['<<^A', '^<<A'], '8': ['<^A', '^<A'], '9': ['^A'],
                        '4': ['<<A'], '5': ['<A'], '6': ['A'],
                        '1': ['v<<A', '<<vA'], '2': ['v<A', '<vA'], '3': ['vA'],
                        '0': ['<vvA', 'vv<A'], 'A': ['vvA']},

                  '1': {'7': ['^^A'], '8': ['>^^A', '^^>A'], '9': ['>>^^A', '^^>>A'],
                        '4': ['^A'], '5': ['>^A', '^>A'], '6': ['>>^A', '^>>A'],
                        '1': ['A'], '2': ['>A'], '3': ['>>A'],
                        '0': ['>vA'], 'A': ['>>vA']},
                  '2': {'7': ['^^<A', '<^^A'], '8': ['^^A'], '9': ['>^^A', '^^>A'],
                        '4': ['^<A', '<^A'], '5': ['^A'], '6': ['>^A', '^>A'],
                        '1': ['<A'], '2': ['A'], '3': ['>A'],
                        '0': ['vA'], 'A': ['>vA', 'v>A']},
                  '3': {'7': ['^^<<A', '<<^^A'], '8': ['^^<A', '<^^A'], '9': ['^^A'],
                        '4': ['^<<A', '<<^A'], '5': ['^<A', '<^A'], '6': ['^A'],
                        '1': ['<<A'], '2': ['<A'], '3': ['A'],
                        '0': ['v<A', '<vA'], 'A': ['vA']},

                  '0': {'7': ['^^^<A'], '8': ['^^^A'], '9': ['>^^^A', '^^^>A'],
                        '4': ['^^<A'], '5': ['^^A'], '6': ['>^^A', '^^>A'],
                        '1': ['^<A'], '2': ['^A'], '3': ['^>A', '>^A'],
                        '0': ['A'], 'A': ['>A']},
                  'A': {'7': ['^^^<<A'], '8': ['^^^<A', '<^^^A'], '9': ['^^^A'],
                        '4': ['^^<<A'], '5': ['^^<A', '<^^A'], '6': ['^^A'],
                        '1': ['^<<A'], '2': ['^<A', '<^A'], '3': ['^A'],
                        '0': ['<A'], 'A': ['A']}
                  }

KEYPAD_PRESSES = {'^': {'^': ['A'], 'A': ['>A'],
                        '<': ['v<A'], 'v': ['vA'], '>': ['v>A', '>vA']},
                  'A': {'^': ['<A'], 'A': ['A'],
                        '<': ['v<<A'], 'v': ['<vA', 'v<A'], '>': ['vA']},

                  '<': {'^': ['>^A'], 'A': ['>>^A'],
                        '<': ['A'], 'v': ['>A'], '>': ['>>A']},
                  'v': {'^': ['^A'], 'A': ['>^A', '^>A'],
                        '<': ['<A'], 'v': ['A'], '>': ['>A']},
                  '>': {'^': ['<^A', '^<A'], 'A': ['^A'],
                        '<': ['<<A'], 'v': ['<A'], '>': ['A']}

                  }


def search(sequence):
    # print(sequence)
    min_len = None
    for s in generate_moves(sequence):
        robot_3_actions, robot_2_actions, robot_1_actions = s
        if min_len is None or len(robot_3_actions) < min_len:
            min_len = len(robot_3_actions)

    # print(min_len, ' ', int(sequence[:-1]))
    return min_len * int(sequence[:-1])


def generate_numpad(sequence):
    robot_position = 'A'
    actions = ['']
    for key in sequence:
        new_actions = []
        robot_1_movements = NUMPAD_PRESSES[robot_position][key]
        for robot_1_movement in robot_1_movements:
            robot_position = key
            new_actions.extend(val + robot_1_movement for val in actions)

        actions = [action for action in new_actions]

    return actions


def generate_keypad(squence):
    robot_position = 'A'
    actions = ['']
    for key in squence:
        new_actions = []
        robot_1_movements = KEYPAD_PRESSES[robot_position][key]
        for robot_1_movement in robot_1_movements:
            robot_position = key
            new_actions.extend(val + robot_1_movement for val in actions)

        actions = [action for action in new_actions]

    return actions


def generate_moves(sequence):
    min_length = None
    min_3_seq = None
    min_2_seq = None
    min_1_seq = None

    for numpad_robot_sequence in generate_numpad(sequence):
        for keypad_robot_1_sequence in generate_keypad(numpad_robot_sequence):
            for keypad_robot_2_sequence in generate_keypad(keypad_robot_1_sequence):
                yield keypad_robot_2_sequence, keypad_robot_1_sequence, numpad_robot_sequence

    '''
                if min_length is None or min_length < len(keypad_robot_2_sequence):
                    min_length = len(keypad_robot_2_sequence)
                    min_3_seq = keypad_robot_2_sequence
                    min_2_seq = keypad_robot_1_sequence
                    min_1_seq = numpad_robot_sequence

    return min_3_seq, min_2_seq, min_1_seq
    '''


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    total = 0
    for sequence in data:
        tmp = search(sequence)
        total += tmp
    print(total)

    assert total < 172288


if __name__ == '__main__':
    main()
