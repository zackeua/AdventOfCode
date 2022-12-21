import sys
import re


def sub(expression: str, patterns: dict) -> str:

    new_expression = expression
    
    while True:
        prev = new_expression
        for pattern, replacement in patterns.items():
            new_expression = re.sub(pattern, f'({replacement})', new_expression)
        if new_expression == prev:
            break

    return new_expression

def main():

    with open(sys.argv[1], 'r') as f:
        data = {elem.split(': ')[0]: elem.split(': ')[1].replace('\n','') for elem in f.readlines()}
        
        
        expression = sub('root', data)
        result = int(eval(expression))
        print(result)

 
if __name__ == '__main__':
    main()
