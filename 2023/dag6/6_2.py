import sys

def search(time, distance):

    total = 0
    for t in range(time+1):
        d = (time-t)*t
        traveled_distance = d if d >= 0 else 0
        if traveled_distance > distance:
            total += 1
    return total


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.split(': ')[1].strip() for line in data]
        times = int(data[0].replace(' ', ''))
        distances = int(data[1].replace(' ', ''))
        total = 1
        for time, distance in zip([times], [distances]):
            ways = 0
            ways += search(time, distance)

            total *= ways

        print(total)


if __name__ == '__main__':
    main()