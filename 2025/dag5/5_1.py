import sys


def is_fresh(ingredient, fresh_itervals):
    for interval in fresh_itervals:
        if interval[0] <= ingredient <= interval[1]:
            return True
    return False


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        # print(data)
    fresh_intervals = []
    avalible_ingredients = []
    for elem in data:
        if elem == "":
            continue
        elif "-" in elem:
            a, b = elem.split("-")
            fresh_intervals.append((int(a), int(b)))
        else:
            avalible_ingredients.append(int(elem))
    # print(fresh_intervals)
    # print(avalible_ingredients)
    number_of_fresh_ingredients = 0
    for ingredient in avalible_ingredients:
        number_of_fresh_ingredients += is_fresh(ingredient, fresh_intervals)

    print(number_of_fresh_ingredients)


if __name__ == "__main__":
    main()
