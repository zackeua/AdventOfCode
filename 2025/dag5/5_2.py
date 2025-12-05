import sys


def new_ingredients(interval, used_intervals):
    if used_intervals == []:
        return interval[1] - interval[0] + 1
    lower, upper = interval

    for used_interval in used_intervals:
        lower_used, upper_used = used_interval
        if lower_used <= lower <= upper_used:
            lower = min(max(lower, upper_used) + 1, upper)

        if lower_used <= upper <= upper_used:
            upper = max(min(upper, lower_used) - 1, lower)
        print(interval, lower, upper)
    return upper - lower + 1


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        last_merged = merged_intervals[-1]

        if interval[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], interval[1])
        else:
            merged_intervals.append(interval)

    return merged_intervals


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
            fresh_intervals.append([int(a), int(b)])
        else:
            avalible_ingredients.append(int(elem))
    # print(fresh_intervals)
    # print(avalible_ingredients)
    number_of_fresh_ingredients = 0
    merged_intervals = merge_intervals(fresh_intervals)
    for interval in merged_intervals:
        number_of_fresh_ingredients += interval[1] - interval[0] + 1

    print(number_of_fresh_ingredients)


if __name__ == "__main__":
    main()
