import sys


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.read()
        data = data.strip()
        for i, elem in enumerate(data[:-14]):
            ok = True
            for offset in range(13):
                if data[i+offset] in data[i+offset+1:i+14]:
                    ok = False
            if ok:
                print(i+14)
                sys.exit()


if __name__ == '__main__':
    main()
