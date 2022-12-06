import sys

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.read()
        data = data.strip()
        for i, elem in enumerate(data[:-4]):
            if data[i] not in data[i+1:i+4] and data[i+1] not in data[i+2:i+4] and data[i+2] != data[i+3]:
                print(i+4)
                sys.exit()

if __name__ == '__main__':
    main()