import sys

def split_molecule(molecule):
    result = []
    temp = molecule[0]
    for elem in molecule[1:]:
        if elem == elem.upper():
            result.append(temp)
            temp = ''
        temp += elem
    result.append(temp)
    return result

def find_configs(rules, molecule):
    unique = set()

    for i, atom in enumerate(molecule):
        temp = [a for a in molecule]
        if atom in rules:
            for replacement in rules[atom]:
                temp[i] = replacement
                unique.add(''.join(temp))

    return unique

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]

molecule = data[-1]

rules = {}

for rule in data[:-2]:
    key, val = rule.split(' => ')
    if key not in rules: rules[key] = []
    rules[key].append(val)

print(rules)
print(molecule)
unique = find_configs(rules, split_molecule(molecule))
print(len(unique))