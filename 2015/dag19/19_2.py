import sys



def get_steps(molecule: str, goal: str, rules: dict):

    steps = 0

    prev = ""
    while molecule != goal:

        for key in rules:
            if key in molecule:
                molecule = molecule.replace(key, rules[key], 1)
                steps += 1
        if molecule == prev:
            return steps
        prev = molecule
    return steps


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [row.replace('\n', '') for row in data]

        molecule = data[-1]

        rules = {}

        for rule in data[:-2]:
            key, val = rule.split(' => ')
            rules[val] = key
        goal = 'e'
        #print(rules)
        #print(molecule)
        print(get_steps(molecule, goal, rules))

if __name__ == '__main__':
    main()
