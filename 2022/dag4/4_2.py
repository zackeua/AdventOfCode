import sys

def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[list(map(int, elem.split('-'))) for elem in  row.split(',')] for row in data]
        count = 0
        for line in data:
            elf1 = line[0]
            elf2 = line[1]
            elf1 = set(range(elf1[0], elf1[1]+1))
            elf2 = set(range(elf2[0], elf2[1]+1))

            count += len(elf1.intersection(elf2)) != 0
    print(count)



if __name__ == '__main__':
    main()
