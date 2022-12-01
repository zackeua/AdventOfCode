import sys

def parse_marker(marker):
    return tuple(map(int, marker[1:-1].split('x')))
    
    
def expand_line(line):
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '(':
            k = 0
            while line[i+k] != ')':
                k += 1
            k += 1
            number_of_chars, count = parse_marker(line[i:i+k])
            result += line[i+k:i+k+number_of_chars]*count
            i = i + k + number_of_chars - 1
        else:
            result += line[i]
        i += 1
    return len(result)

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    print(sum([expand_line(line) for line in data]))
        