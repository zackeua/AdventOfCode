import sys

import heapq


def get_steps(molecule: str, goal: str, rules: dict):

    visited = set()
    while molecule != []:
        #result, old_molecule = molecule[0]
        #molecule = molecule[1:]

        result, old_molecule = heapq.heappop(molecule)

        visited.add(old_molecule)

        for key in rules:
            if rules[key] != 'e':                
                current_molecule = old_molecule.replace(key, rules[key], 1)
                if current_molecule not in visited:
                    heapq.heappush(molecule, (1 + result, current_molecule))
                    #molecule.append((1 + result, current_molecule))
                #print(old_molecule, current_molecule, key, rules[key])

            elif old_molecule == key:
                old_molecule = 'e'
                #print(old_molecule, current_molecule, key, rules[key])
                return result + 1
        #print(molecule)
        #input()
        #molecule.sort()

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [row.replace('\n', '') for row in data]

        molecule = data[-1]

        rules = {}

        for rule in data[:-2]:
            val, key = rule.split(' => ')
            rules[key[::-1]] = val[::-1]
        queue = [(0, molecule[::-1])]
        heapq.heapify(queue)
        goal = 'e'
        print(rules)
        print(molecule)
        print(get_steps(queue, goal, rules))

if __name__ == '__main__':
    main()
