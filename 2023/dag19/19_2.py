import sys


class SingleRange:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __add__(self, other):
        # if ranges overlap, return the range that covers both
        if self.start <= other.start and self.end <= other.end:
            return SingleRange(self.start, other.end)
        if other.start <= self.start and other.end <= self.end:
            return SingleRange(other.start, self.end)
        # if ranges don't overlap, return None
        if self.end <= other.start or other.end <= self.start:
            return None
        if self.start <= other.start and other.end <= self.end:
            return self
        if other.start <= self.start and self.end <= other.end:
            return other


class MyRange:

    def __init__(self, ranges=[]):
        self.ranges = ranges

    def __add__(self, other):
        self.ranges.extend(other.ranges)
        new_ranges = []
        while self.ranges != new_ranges:
            new_ranges = []
            for i in range(len(self.ranges)):
                for j in range(i+1, len(self.ranges)):
                    new_range = self.ranges[i] + self.ranges[j]
                    if new_range is not None:
                        new_ranges.append(new_range)
                    else:
                        new_ranges.append(self.ranges[i])
                        new_ranges.append(self.ranges[j])
            self.ranges = [tmp_range for tmp_range in new_ranges]


    def apply_filter(self, filter):
        new_ranges = []
        for tmp_range in self.ranges:
            if filter(tmp_range):
                new_ranges.append(tmp_range)
        self.ranges = new_ranges

def check_rule(expression, x, m, a, s, parts):
    expression = expression.split(':')
    if len(expression) == 1: # accept or reject
        return expression[0]
    if eval(expression[0]): # if condition is true
        return expression[1]
    return None # if condition is false


def forward_sets(current_workflow, part, all_workflows):

    ranges = {x: MyRange(), m: MyRange(), a: MyRange(), s: MyRange()}
    for rule in workflows[workflow_name]:
        status, allow_range, complement_range = check_rule(rule, **part)
        if status is None: # if current condition is not met, continue wth complement range
            continue
        elif 'R' in status:
            break
        elif 'A' in status:
            total += sum(part.values())
            break
        else:
            workflow_name = status
            ranges = forward_sets(workflow_name, part, all_workflows)
            break


    return ranges

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

        part = {'x': range(1, 4001), 'm': range(1, 4001), 'a': range(1, 4001), 's': range(1, 4001)}
        current_workflow = 'in'
        forward_sets(workflow_name, part, workflows)
        print(total)


if __name__ == '__main__':
    main()
