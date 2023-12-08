import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        moves = data[0].strip()
        next_element_map = {}
        for line in data[2:]:
            current, next_elements = line.split(' = ')
            left_element, right_element = next_elements[1:-1].split(', ')
            tmp = {'L': left_element, 'R': right_element}
            next_element_map[current] = tmp
        
        steps = 0
        current_element = 'AAA'
        while current_element != 'ZZZ':
            next_direction = moves[steps % len(moves)]
            current_element = next_element_map[current_element][next_direction]

            steps += 1

        print(steps)


if __name__ == '__main__':
    main()