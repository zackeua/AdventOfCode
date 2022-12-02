import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        #print(data)
        score = 0
        for row in data:
            if 'A' in row:  # A = Rock
                if 'X' in row: # loose
                    score += 0 + 3
                if 'Y' in row:  # draw
                    score += 3 + 1
                if 'Z' in row:  # win
                    score += 6 + 2
            if 'B' in row:  # B = Paper
                if 'X' in row: # loose
                    score += 0 + 1
                if 'Y' in row:  # draw
                    score += 3 + 2
                if 'Z' in row:  # win
                    score += 6 + 3
            if 'C' in row:  # C = Scissors
                if 'X' in row:  # loose
                    score += 0 + 2
                if 'Y' in row:  # draw
                    score += 3 + 3
                if 'Z' in row:  # win
                    score += 6 + 1
            #print(score)
        print(score)


if __name__ == '__main__':
    main()
