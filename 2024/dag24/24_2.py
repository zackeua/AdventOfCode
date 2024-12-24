import sys
import operator
import itertools

OPERATOR = {'AND': operator.and_, 'OR': operator.or_, 'XOR': operator.xor}


def z_connections_active(connections):
    for signal in connections:
        _, _, _, out = signal
        if out[0] == 'z':
            return False

    return True


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    connections = []
    current_signals = {}

    parse_connections = False
    change_map = {}
    change_map['fkb'] = 'z16'
    change_map['z16'] = 'fkb'
    change_map['z31'] = 'rdn'
    change_map['rdn'] = 'z31'
    change_map['z37'] = 'rrn'
    change_map['rrn'] = 'z37'
    change_map['rqf'] = 'nnr'
    change_map['nnr'] = 'rqf'

    for line in data:
        if line == '':
            parse_connections = True
        elif parse_connections:
            in1, op, in2, _, out = line.split(' ')
            out = change_map.get(out, out)
            current_signals[out] = (in1, op, in2)
        else:
            in1, val = line.split(': ')
            current_signals[in1] = in1  # True if val == '1' else False

    z_keys = sorted(itertools.filterfalse(
        lambda x: x[0] != 'z', current_signals.keys()))
    for key in z_keys:
        signal = current_signals[key]
        print(key, ': ', signal)
        if signal[0][0] not in ['x', 'y']:
            signal_1 = current_signals[signal[0]]
            print('\t', signal[0], ': ', signal_1)
            if signal_1[0][0] not in ['x', 'y']:
                print('\t\t', signal_1[0], ': ', current_signals[signal_1[0]])
            if signal_1[2][0] not in ['x', 'y']:
                print('\t\t', signal_1[2], ': ', current_signals[signal_1[2]])

        if signal[2][0] not in ['x', 'y']:
            signal_1 = current_signals[signal[2]]
            print('\t', signal[2], ': ', current_signals[signal[2]])
            if signal_1[0][0] not in ['x', 'y']:
                print('\t\t', signal_1[0], ': ', current_signals[signal_1[0]])
            if signal_1[2][0] not in ['x', 'y']:
                print('\t\t', signal_1[2], ': ', current_signals[signal_1[2]])

    print(','.join(sorted(change_map.keys())))


if __name__ == '__main__':
    main()
