import sys


def get_val(registers, arg):
    if arg < 4:
        return arg
    if arg == 4:
        return registers[4]
    if arg == 5:
        return registers[5]
    if arg == 6:
        return registers[6]


def computer(program, registers, program_counter):

    output = []
    # prev_program_counter = -1
    try:
        while True:
            # if program_counter == prev_program_counter:
            # return ','.join(output)
            # prev_program_counter = program_counter
            if program_counter < 0 or program_counter > len(program):
                # print(','.join(output))
                output
                # break
            # print(program_counter)
            if program[program_counter] == 0:
                # adv operator:
                numerator = registers[4]  # A
                exponent = get_val(registers, program[program_counter + 1])
                denomarator = 2 ** exponent
                registers[4] = numerator // denomarator
                program_counter += 2
            elif program[program_counter] == 1:
                registers[5] = registers[5] ^ program[program_counter + 1]
                program_counter += 2
            elif program[program_counter] == 2:
                value = get_val(registers, program[program_counter + 1])
                registers[5] = value % 8
                program_counter += 2
            elif program[program_counter] == 3:
                if registers[4] == 0:
                    program_counter += 2
                else:
                    program_counter = program[program_counter + 1]
            elif program[program_counter] == 4:
                registers[5] = registers[5] ^ registers[6]
                program_counter += 2
            elif program[program_counter] == 5:
                val = get_val(registers, program[program_counter + 1])
                output.append(val % 8)
                program_counter += 2
            elif program[program_counter] == 6:
                numerator = registers[4]  # A
                exponent = get_val(registers, program[program_counter + 1])
                denomarator = 2 ** exponent
                registers[5] = numerator // denomarator
                program_counter += 2
            elif program[program_counter] == 7:
                numerator = registers[4]  # A
                exponent = get_val(registers, program[program_counter + 1])
                denomarator = 2 ** exponent
                registers[6] = numerator // denomarator
                program_counter += 2
            else:
                assert False
    except:
        # print(','.join(output))
        return output
    return output


def search(depth, val, program, registers, tmp=[]):
    if depth == -1:
        return val, tmp
    for i in range(0, 8):
        a_val = val + i * 8 ** depth
        registers[4] = a_val
        registers[5] = 0
        registers[6] = 0
        program_counter = 0
        tmp = computer(program, registers, program_counter)
        if len(tmp) == len(program):
            all_equal = True
            for j in range(depth, len(program)):
                if tmp[j] != program[j]:
                    all_equal = False
            if all_equal:
                return search(depth - 1, a_val, program, registers, tmp)


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        # print(data)

    registers = {}
    program = []
    program_counter = 0
    parse_register = True
    for line in data:
        if line == '':
            parse_register = False
        elif parse_register:
            _, key, val = line.split()
            k = key[0]
            k = ord(k) - ord('A') + 4
            registers[k] = int(val)
        else:
            program = list(map(int, line.split()[1].split(',')))

    a_val = 0
    a_val, tmp = search(15, 0, program, registers)

    print(a_val)
    assert len(tmp) == len(program)
    assert program[15] == tmp[15], f'{program[15]} {tmp[15]}'
    assert program[14] == tmp[14], f'{program[14]} {tmp[14]}'
    assert program[13] == tmp[13], f'{program[13]} {tmp[13]}'
    assert program[12] == tmp[12], f'{program[12]} {tmp[12]}'
    assert program[11] == tmp[11], f'{program[11]} {tmp[11]}'
    assert program[10] == tmp[10], f'{program[10]} {tmp[10]}'
    assert program[9] == tmp[9], f'{program[9]} {tmp[9]}'
    assert program[8] == tmp[8], f'{program[8]} {tmp[8]}'
    assert program[7] == tmp[7], f'{program[7]} {tmp[7]}'
    assert program[6] == tmp[6], f'{program[6]} {tmp[6]}'
    assert program[5] == tmp[5], f'{program[5]} {tmp[5]}'
    assert program[4] == tmp[4], f'{program[4]} {tmp[4]}'
    assert program[3] == tmp[3], f'{program[3]} {tmp[3]}'
    assert program[2] == tmp[2], f'{program[2]} {tmp[2]}'
    assert program[1] == tmp[1], f'{program[1]} {tmp[1]}'
    assert program[0] == tmp[0], f'{program[0]} {tmp[0]}'


if __name__ == '__main__':
    main()
