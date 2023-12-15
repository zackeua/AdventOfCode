import sys



def hashing(string: str ):
    current = 0
    for val in string:
        ascii_code = ord(val)
        current += ascii_code
        current *= 17
        current %= 256
    return current

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readline()
        data = data.strip()
        data = data.split(',')
        total = 0
        for string in data:
            total += hashing(string)
        print(total)
    

if __name__ == '__main__':
    main()

