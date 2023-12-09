import sys

from math import lcm


def reduce_pairwise_coprime(numbers):
    gcd_value = numbers[0]
    for num in numbers[1:]:
        gcd_value = gcd(gcd_value, num)

    reduced_numbers = [num // gcd_value for num in numbers] + [gcd_value]
    return reduced_numbers


def is_finished(data):
    for element in data:
        if element is None:
            return False

    return True


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        moves = data[0].strip()
        next_element_map = {}
        current_elements = []
        for line in data[2:]:
            current, next_elements = line.split(' = ')
            left_element, right_element = next_elements[1:-1].split(', ')
            tmp = {'L': left_element, 'R': right_element}
            next_element_map[current] = tmp
            if current[2] == 'A':
                current_elements.append(current)

        steps = 0

        cycles = [None] * len(current_elements)

        while not is_finished(cycles):
            for i, elem in enumerate(current_elements):
                next_direction = moves[steps % len(moves)]
                current_elements[i] = next_element_map[elem][next_direction]
                if current_elements[i][2] == 'Z':
                    # print(i, steps+1)
                    if cycles[i] is None:
                        cycles[i] = steps+1

            steps += 1

        answer = lcm(*cycles)

        print(answer)

        for c in cycles:
            # print(answer % c)
            assert answer % c == 0


if __name__ == '__main__':
    main()
