import sys


class SingleRange:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
        if start == 0 and end == 0:
            self.start = None
            self.end = None

    def __add__(self, other):
        if self is None or self.start is None or self.end is None:
            return other
        if other is None or other.start is None or other.end is None:
            return self
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

    def __radd__(self, other):
        return self.__add__(other)

    def apply_filter(self, operator, value):
        if operator == '<':
            if self.end < value:
                return self
            elif self.start < value and value < self.end:
                return SingleRange(self.start, value-1)
            else:
                return None
        if operator == '>':
            if value < self.start:
                return self
            elif self.start < value and value < self.end:
                return SingleRange(value+1, self.end)
            else:
                return None

    def apply_reverse_filter(self, operator, value):
        # print('apply_reverse_filter', operator, value)
        if operator == '<':
            return self.apply_filter('>', value-1)
        if operator == '>':
            return self.apply_filter('<', value+1)

    def __str__(self):
        return f'[{self.start}, {self.end}]'

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return SingleRange(self.start, self.end)


class MyRange:

    def __init__(self, ranges=None):
        if ranges is None:
            self.ranges = [SingleRange()]
        else:
            self.ranges = ranges

    def __add__(self, other):
        if other is None:
            return self
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
            self.ranges = [tmp_range for tmp_range in new_ranges if tmp_range != SingleRange()]
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def apply_filter(self, operator, value, reverse=False):
        new_ranges = []
        for tmp_range in self.ranges:
            if reverse:
                new_range = tmp_range.apply_reverse_filter(operator, value)
            else:
                new_range = tmp_range.apply_filter(operator, value)
            if new_range is not None:
                new_ranges.append(new_range)
        self.ranges = new_ranges
        return self

    def apply_reverse_filter(self, operator, value):
        return self.apply_filter(operator, value, reverse=True)

    def total(self):
        total = 0
        # print('total')
        # print(self.ranges)
        for tmp_range in self.ranges:
            if tmp_range == SingleRange():
                continue
            # print(tmp_range.start, tmp_range.end, tmp_range.end - tmp_range.start + 1)
            total += tmp_range.end - tmp_range.start + 1

        return total

    def __str__(self):
        return str(self.ranges)

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return MyRange([tmp_range.__copy__() for tmp_range in self.ranges])


def check_rule(expression):
    expression = expression.split(':')
    if len(expression) == 1:  # accept or reject
        return expression[0], None
    if len(expression) == 2:
        return expression[0], expression[1]


def forward_sets(current_workflow, part, all_workflows):
    # print(f'{current_workflow = }, {part = }')
    if current_workflow == 'A':
        total = 1
        for key, value in part.items():
            total *= value.total()
        return total
    if current_workflow == 'R':
        return 0

    total = 0

    for rule in all_workflows[current_workflow]:
        status = check_rule(rule)
        # print(f'{status = }')
        # print(f'{all_workflows[current_workflow] = }')
        match status:
            case ('A', None):
                local = 1
                for key, value in part.items():
                    local *= value.total()
                total += local
            case ('R', None):
                pass
            case (dest, None):
                new_part = {key: value.__copy__() for key, value in part.items()}
                total += forward_sets(dest, new_part, all_workflows)
            case (rule, dest):
                variable, operator, value = rule[0], rule[1], int(rule[2:])
                # print(variable, operator, value)
                new_part = {key: value.__copy__() for key, value in part.items()}
                new_part[variable] = new_part[variable].apply_filter(operator, value)
                part[variable] = part[variable].apply_reverse_filter(operator, value)
                total += forward_sets(dest, new_part, all_workflows)
            case _:
                assert False  # should not happen
    return total


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

        part = {'x': MyRange([SingleRange(1, 4000)]), 'm': MyRange([SingleRange(1, 4000)]),
                'a': MyRange([SingleRange(1, 4000)]), 's': MyRange([SingleRange(1, 4000)])}
        current_workflow = 'in'
        total = forward_sets(current_workflow, part, workflows)
        # print('calculating total')
        print(total)
        assert total > 57820124122176
        assert total < 43584967506249734436144
        assert total != 9565598402393996


if __name__ == '__main__':
    main()
