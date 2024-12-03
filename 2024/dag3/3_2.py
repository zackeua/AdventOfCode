import sys
import re

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

    mul_identifyer = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')

    result = 0
    multiply = True
    for line in data:
        matches = mul_identifyer.findall(line)

        for m in matches:
            if m == 'do()':
                multiply = True
            elif m == 'don\'t()':
                multiply = False
            elif multiply:
                n = m.replace('mul(','').replace(')', '')
                a, b = list(map(int, n.split(',')))
                result += a * b

    print(result)




if __name__ == '__main__':
    main()
