import sys


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

        total_priority = 0
        
        for i in range(0, len(data), 3):
            l1 = data[i]
            l2 = data[i+1]
            l3 = data[i+2]
            notAdded = True
            for c in l1:
                if c in l2 and c in l3 and notAdded:
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
