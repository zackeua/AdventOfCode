import sys

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[list(map(int, elem.split('-'))) for elem in  row.split(',')] for row in data]
        count = 0
        for line in data:
            elf1 = line[0]
            elf2 = line[1]
            if elf1[0] <= elf2[0] and elf2[1] <= elf1[1] or elf2[0] <= elf1[0] and elf1[1] <= elf2[1]:
                count += 1
    print(count)



if __name__ == '__main__':
    main()