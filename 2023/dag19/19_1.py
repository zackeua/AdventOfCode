import sys


def check_rule(expression, x, m, a, s):
    expression = expression.split(':')
    if len(expression) == 1:
        return expression[0]
    if eval(expression[0]):
        return expression[1]
    return None


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

        total = 0
        for part in parts:
            # print(part)
            workflow_name = 'in'
            status = ''
            while 'A' != status and 'R' != status or status == '':
                # print(f'{status = }')
                for rule in workflows[workflow_name]:
                    status = check_rule(rule, **part)
                    # print([status])
                    # print(workflow_name, part, status)
                    if status is None:
                        continue
                    elif 'R' in status:
                        break
                    elif 'A' in status:
                        total += sum(part.values())
                        break
                    else:
                        workflow_name = status
                        break
        print(total)


if __name__ == '__main__':
    main()
