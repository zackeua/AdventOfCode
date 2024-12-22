import sys


def calculate_secret_number(number):

    # step 1:
    n = (number * 64)
    n = number ^ n
    n = n % 16777216

    # step 2:
    m = n // 32
    n = n ^ m
    n = n % 16777216

    # step 3:
    m = n * 2048
    n = n ^ m
    n = n % 16777216
    return n


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [int(line.strip()) for line in data]

    total = 0
    for number in data:
        i = 0
        secret = number
        while i < 2000:
            secret = calculate_secret_number(secret)
            i += 1
        total += secret
        # print(f'{number}: {secret}')
    print(total)


if __name__ == '__main__':
    main()
