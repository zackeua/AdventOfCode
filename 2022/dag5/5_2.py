import sys


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        stacks = None
        ops_start = 0 
        for index, line in enumerate(data):
            if '[' in line:
                chars = line[:-1][1::4]
                if stacks is None:
                    stacks = [[] for _ in chars]
                for i , c in enumerate(chars):
                    if c != ' ': stacks[i].append(c)
                ops_start = index + 3

        data = data[ops_start:]

        for line in data:
            split_line = line.split()
            count = int(split_line[1])
            from_stack = int(split_line[3]) - 1
            to_stack = int(split_line[5]) - 1

            elements_to_move = stacks[from_stack][:count]
            stacks[from_stack] = stacks[from_stack][count:]
            #print(elements_to_move)
            elements_to_move.extend(stacks[to_stack])
            stacks[to_stack] = elements_to_move

        for row in stacks:
            print(row[0], end='')
        print()


if __name__ == '__main__':
    main()
