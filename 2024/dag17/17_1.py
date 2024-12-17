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
    try:
        while True:
            if program_counter < 0 or program_counter > len(program):
                print(','.join(output))
                break
            # print(program_counter)
            if program[program_counter] == 0:
                # adv operator:
                numerator = registers[4]  # A
                exponent = get_val(registers, program[program_counter + 1])
                denomarator = 2 ** exponent
                res = numerator
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
                    program_counter += 0
                else:
                    program_counter = program[program_counter + 1]
            elif program[program_counter] == 4:
                registers[5] = registers[5] ^ registers[6]
                program_counter += 2
            elif program[program_counter] == 5:
                val = get_val(registers, program[program_counter + 1])
                output.append(str(val % 8))
                print(','.join(output))
                program_counter += 2
            elif program[program_counter] == 6:
                numerator = registers[5]  # A
                exponent = get_val(registers, program[program_counter + 1])
                denomarator = 2 ** exponent
                res = numerator
                registers[4] = numerator // denomarator
                program_counter += 2
            elif program[program_counter] == 7:
                numerator = registers[6]  # A
                exponent = get_val(registers, program[program_counter + 1])
                denomarator = 2 ** exponent
                res = numerator
                registers[4] = numerator // denomarator
                program_counter += 2
            else:
                assert False
    except:
        print(','.join(output))


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        print(data)

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

    computer(program, registers, program_counter)


if __name__ == '__main__':
    main()
