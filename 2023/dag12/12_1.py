import sys
import re

def replace_unknown(text: str):
    if '?' not in text:
        return [text]
    

    tmp1 = text.replace('?', '#', 1)
    tmp2 = text.replace('?', '.', 1)
    result = replace_unknown(tmp1)
    result.extend(replace_unknown(tmp2))

    return result

def create_regex(pattern:str):
    numbers = list(map(int, pattern.split(',')))
    regex_pattern = '^\.*' +'\.+'.join(['#'*number for number in numbers]) + '\.*$'
    return regex_pattern
    


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip().split() for line in data]
        total = 0
        for springs, pattern in data:
            regex_pattern = create_regex(pattern)
            regex_matcher = re.compile(regex_pattern)
            #print(springs, pattern, regex_pattern)
            for spring in replace_unknown(springs):
                result = regex_matcher.match(spring)
                if result is not None:
                    #print(spring, regex_pattern)  
                    total += 1
                
        print(total)

if __name__ == '__main__':
    main()