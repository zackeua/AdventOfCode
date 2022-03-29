
class Sue:
    def __init__(self, tups) -> None:
        d = {'children': 3, 'cats': 7,
              'samoyeds': 2, 'pomeranians': 3,
              'akitas': 0, 'vizslas': 0,
              'goldfish':5, 'trees': 3,
              'cars': 2, 'perfumes': 1}
        
        self._valid = True
        for tup in tups:
            if d[tup[0]] != tup[1]:
                self._valid = False
    
    def is_valid(self):
        return self._valid


with open('input.txt', 'r') as f:
    data = f.readlines()

def m(s):
    return s[0].upper() + s[1:]
with open('output.txt', 'w') as f:
    Sues = []
    for row in data:
        split1, *split2 = row.split(', ')

        split1, *a = split1.split(': ')
        a = ': '.join(a)
        split2.insert(0, a)
        idx = int(split1[4:])
        things = []
        for item in split2:
            thing, count = item.split(': ')
            things.append((thing, int(count)))
        Sues.append(Sue(things))

for i, sue in enumerate(Sues, 1):
    if sue.is_valid():
        print(i)
