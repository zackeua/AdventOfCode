import sys
import re

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

    mul_identifyer = re.compile(r'mul\(\d+,\d+\)')

    result = 0
    for line in data:
        matches = mul_identifyer.findall(line)

        for m in matches:
            n = m.replace('mul(','').replace(')', '')
            a, b = list(map(int, n.split(',')))
            result += a * b

    print(result)




if __name__ == '__main__':
    main()
