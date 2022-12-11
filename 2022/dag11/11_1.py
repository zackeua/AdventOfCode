import sys

from functools import partial
debug = False


def debug_print(*s, **args):
    if debug:
        print(*s, **args)


def update_func(old, monkey, update_rule, send_rule, true_list, false_list):
    new = update_rule[monkey](old)

    new = int(new/3)

    if new % send_rule[monkey] == 0:
        return new, true_list[monkey]
    else:
        return new, false_list[monkey]

add = lambda b, a: a + b
mul = lambda b, a: a * b
power = lambda a,: a * a


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        monkey_items = [list(map(int, row.split(': ')[1].split(', '))) for row in data[1::7]]
        update_rule = []
        for line in data[2::7]:
            print(line)
            sub_line = line.split(' = ')[1]
            if sub_line == 'old * old':
                update_rule.append(power)
            elif '*' in sub_line:
                update_rule.append(partial(mul, int(sub_line.split('*')[-1])))
                print(update_rule[-1](1))
            else:
                update_rule.append(partial(add, int(sub_line.split('+')[-1])))
                print(update_rule[-1](1))

        send_rule = [int(row.split(' ')[-1]) for row in data[3::7]]
        monkey_true_list = [int(row[-1]) for row in data[4::7]]
        monkey_false_list = [int(row[-1]) for row in data[5::7]]

        print(monkey_items)
        print(update_rule)
        print(send_rule)
        print(monkey_true_list)
        print(monkey_false_list)


    monkey_inspect_count = [0]*len(monkey_items)
    for round in range(1, 21):
        for monkey in range(len(monkey_items)):
            new_monkey_items = []
            debug_print(f'Monkey {monkey}:')
            for worry in monkey_items[monkey]:
                debug_print(f'  Monkey inspects an item with a worry level of {worry}.')
                next_worry, next_monkey = update_func(worry, monkey, update_rule, send_rule, monkey_true_list, monkey_false_list)
                monkey_inspect_count[monkey] += 1
                if monkey == next_monkey:
                    new_monkey_items.append(next_worry)
                else:
                    monkey_items[next_monkey].append(next_worry)
            monkey_items[monkey] = new_monkey_items
        debug_print(f'After round {round}, the monkeys are holding items with these worry levels:')
        for monkey in range(len(monkey_items)):
            debug_print(f'Monkey {monkey}: {", ".join(list(map(str,monkey_items[monkey])))}')
    print(monkey_inspect_count)
    monkey_inspect_count.sort()
    print(monkey_inspect_count[-1] * monkey_inspect_count[-2])
if __name__ == '__main__':
    main()
