import sys
import itertools

def search(line: list):
    
    if sum(elem == 0 for elem in line) == len(line):
        return line

    difference_line = []
    
    for pair in itertools.pairwise(line):
        
        difference_line.append(pair[1] - pair[0])

    difference_line = search(difference_line)

    line.insert(0, line[0] - difference_line[0])

    return line

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [list(map(int, line.split()))  for line in data]
        
        
        answer = 0

        for line in data:

            new_line = search(line)
            answer += new_line[0]

        print(answer)


if __name__ == '__main__':
    main()