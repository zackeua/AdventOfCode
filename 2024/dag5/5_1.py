import sys
from functools import cmp_to_key

def expand_rules(d):
    for r in d.keys():
        loop = True
        while loop:
            len_d = len(d[r])
            for k in d[r]:
                if k in d:
                    for v in d[k]:
                        if v not in d[r]:
                            d[r].append(v)
            if len_d != len(d.keys()):
                loop = False
    return d


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        print(data)
        page_prdering_rule_data = [elem for elem in data if '|' in elem]
        update_data = [elem for elem in data if ',' in elem]

        page_prdering_rule_data = [list(map(int, elem.split('|'))) for elem in page_prdering_rule_data]
        update_data = [list(map(int, elem.split(','))) for elem in update_data]
            
        page_ordering_rules = {}
        for page_rule in page_prdering_rule_data:
            if page_rule[0] not in page_ordering_rules:
                page_ordering_rules[page_rule[0]] = [] 
            page_ordering_rules[page_rule[0]].append(page_rule[1])


        #print(page_ordering_rules)
        #for _ in range(len(page_ordering_rules.keys())):
        #page_ordering_rules = expand_rules(page_ordering_rules)
    
        def cmp_function(a, b):
            if a in page_ordering_rules:
                if b in page_ordering_rules[a]:
                    return -1
                return 0
            return 0 

        print(page_ordering_rules)
        result = 0
        for update_rule in update_data:
            sorted_update_rule = sorted(update_rule, key=cmp_to_key(cmp_function))
            correctly_sorted = True
            for a, b in zip(update_rule, sorted_update_rule):
                if a != b:
                    correctly_sorted = False
                    break
            if correctly_sorted:
                print(update_rule)
                print(sorted_update_rule)
                assert len(sorted_update_rule) % 2 == 1
                result += sorted_update_rule[len(sorted_update_rule) // 2]
        print(result)

           





if __name__ == '__main__':
    main()
