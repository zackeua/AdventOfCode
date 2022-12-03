import sys

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

        total_priority = 0
        for line in data:
            mid = len(line)//2
            notAdded = True
            for c in line[:mid]:
                if c in line[mid:] and notAdded:
                    priority = 0
                    notAdded = False
                    if c.islower():
                        priority += ord(c) - 96
                    else:
                        priority += ord(c) - 38
                    total_priority += priority
                    #print(priority, c)
        print(total_priority)
if __name__ == '__main__':
    main()