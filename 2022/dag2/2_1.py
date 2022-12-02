import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        #print(data)
        score = 0
        for row in data:
            if 'Y' in row:  # Y = Paper
                score += 2
                if 'A' in row:  # A = Rock
                    score += 6
                if 'B' in row:  # B = Paper
                    score += 3
            if 'X' in row:  # X = Rock
                score += 1
                if 'A' in row:
                    score += 3
                if 'C' in row:
                    score += 6
            if 'Z' in row:  # Z = Scissors
                score += 3
                if 'B' in row:
                    score += 6
                if 'C' in row:
                    score += 3
        print(score)

if __name__ == '__main__':
    main()
