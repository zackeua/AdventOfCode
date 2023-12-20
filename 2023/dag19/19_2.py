import sys
from minizinc import Instance, Model, Solver


def generate_minizinc_constraint(workflows):
   
    current_workflow = 'in'
    for rule in workflows[current_workflow]:
        cond, true_case, false_case = get_condition(rule)
        print(cond, true_case, false_case)
        minizinc_if_statement = f'if {cond} then {true_case} else {false_case} endif;'
        

def minizinc_constraint_expression(expression):
    expression = expression.split(':')
    if len(expression) == 1: # accept or reject
        if expression[0] == 'A':
            return 'true', 'true'
        elif expression[0] == 'R':
            return 'false', 'false'
        else:
            return expression[0], 'false', True
    return expression[0], expression[1], True

"""

def solve(workflows):
    gecode = Solver.lookup("gecode")
    model = Model()
    
    # add variables
    model.add_string("""
    var 1..100: x;
    var 1..100: m;
    var 1..100: a;
    var 1..100: s;
    """)


    
    # add constraints
    model.add_string("""
    constraint x = 1;
    constraint m = 2;
    constraint a = 3;
    constraint s = 4;
    """)

    # add objective
    model.add_string("""
    solve satisfy; 
    """)
    instance = Instance(gecode, model)

    # find all possible combinations of parts
    result = instance.solve(all_solutions=True)
    print(len(result))
    


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
    solve(workflows)


if __name__ == '__main__':
    main()
