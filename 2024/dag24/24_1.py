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
    for line in data:
        if line == '':
            parse_connections = True
        elif parse_connections:
            in1, op, in2, _, out = line.split(' ')
            connections.append((in1, op, in2, out))
        else:
            in1, val = line.split(': ')
            current_signals[in1] = True if val == '1' else False

    while not z_connections_active(connections):
        signal = connections[0]
        connections = connections[1:]
        in1 = current_signals.get(signal[0], None)
        op = OPERATOR.get(signal[1])
        in2 = current_signals.get(signal[2], None)
        out = signal[3]
        if in1 is None or in2 is None:
            connections.append(signal)
        else:
            if signal[1] == 'AND':
                current_signals[out] = in1 and in2
            if signal[1] == 'OR':
                current_signals[out] = in1 or in2
            if signal[1] == 'XOR':
                current_signals[out] = in1 ^ in2
            # current_signals[out] = op(in1, in2)

    binary_string = ''
    z_keys = sorted(itertools.filterfalse(
        lambda x: x[0] != 'z', current_signals.keys()), reverse=True)
    for key in z_keys:
        binary_string += '1' if current_signals[key] else '0'

    result = int(binary_string, base=2)
    print(result)


if __name__ == '__main__':
    main()
