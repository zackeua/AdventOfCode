import sys
import re
import tqdm
import functools


DAMAGED = '#'
OPERATIONAL = '.'
UNKNOWN = '?'

# global matcher

@functools.lru_cache()
def matches(text: str, pattern: list[int], prev='.', debug_str=()):
    if len(pattern) == 0:
        if DAMAGED not in text:
            # global matcher
            #if matcher.match(''.join(debug_str) + text) is None:
            #    print(''.join(debug_str) + text)
            #    sys.exit(0)
            #    # print(debug_str + text)
            # assert debug_str != ''
            # print(debug_str + text)
            return 1
        return 0
    if len(text) == 0:
        return 0
    part = text[:pattern[0]]
    # print(text, pattern, part)
    # input()
    total = 0
    # matches the # and ? in the pattern
    if prev != DAMAGED and OPERATIONAL not in part and len(part) == pattern[0]:
        # print(part, pattern, text)
        # The # has to be separated by . or ?
        if pattern[0] < len(text) and DAMAGED != text[pattern[0]]:
            total += matches(text[pattern[0]+1:], pattern[1:], text[pattern[0]]) #, debug_str + ('#'*pattern[0] + '.',))
        # if match is at the end of the text, there is nothing to the right
        elif pattern[0] == len(text) and len(pattern) == 1:
            total += matches(text[pattern[0]+1:], pattern[1:], '.') #, debug_str + ('#'*pattern[0],))
    # assume the pattern did not match, try again
    if prev != DAMAGED:
        total += matches(text[1:], pattern, text[0]) #, debug_str + (text[0],))
    return total


def generate_matcher(pattern: list[int], length: int):
    regex = ''
    m = r'[.?]+'.join(r'[?#]'*p for p in pattern)

    regex = r'^[.?]*' + r'[.?]+'.join([m]*length) + r'[.?]*$'

    return re.compile(regex)

def main():

    with open(sys.argv[1], 'r') as f:
        # global matcher
        data = f.readlines()
        data = [line.strip().split() for line in data]
        total = 0
        repetitions = 5
        for springs, pattern in tqdm.tqdm(data):
            local = 0
            pattern = tuple(map(int, pattern.split(',')))
            extended_springs = '?'.join([springs]*repetitions)
            # matcher = generate_matcher(pattern, repetitions)
            local = matches(extended_springs, pattern*repetitions)
            total += local
            # print(f'{springs}, {pattern} : {extended_springs}, {pattern * repetitions} : {local}')
        print(total)
        assert total < 203284796184157
        assert total < 1907721526566707227243


if __name__ == '__main__':
    main()
