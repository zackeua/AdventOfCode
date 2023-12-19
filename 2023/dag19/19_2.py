import sys


def generate_minizinc_file(workflows):
    #with open('minizinc_file.mzn', 'w') as f:
    with sys.stdout as f:
        print('include "globals.mzn";', file=f)
        print('var 1..4000: x;', file=f)
        print('var 1..4000: m;', file=f)
        print('var 1..4000: a;', file=f)
        print('var 1..4000: s;', file=f)
   
        current_workflow = 'in'
        for rule in workflows[current_workflow]:
            
            cond, else_case, should_replace = get_condition(rule)
            print(cond, else_case, should_replace)
            if should_replace:

                else_case = else_case.replace('x', 'x')
            minizinc_if_statement = f'if {cond} then true else {else_case} endif;'
            print(minizinc_if_statement, file=f)

def get_condition(expression):
    expression = expression.split(':')
    if len(expression) == 1: # accept or reject
        if expression[0] == 'A':
            return 'true', 'false', False
        elif expression[0] == 'R':
            return 'false', 'true', False
        else:
            return expression[0], 'false', True
    return expression[0], expression[1], True


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

        workflows = {}
        parsing_workflow = True
        parts = []
        for line in data:
            if line == '':
                parsing_workflow = False
                continue

            if parsing_workflow:
                name, rest = line.split('{')
                rule_list = rest[:-1].split(',')
                rules = []
                for rule in rule_list:
                    # print(name, rule)
                    rules.append(rule)
                workflows[name] = rules
            else:
                part = {}
                ratings = line[1:-1].split(',')
                for rating in ratings:
                    key, value = rating.split('=')
                    part[key] = int(value)
                parts.append(part)

    generate_minizinc_file(workflows)


if __name__ == '__main__':
    main()
