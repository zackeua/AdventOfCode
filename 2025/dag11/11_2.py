import sys
import functools

global graph


@functools.lru_cache
def search(start, target):
    global graph
    if start == target:
        return 1
    if start == "out":
        return 0
    total = 0
    for node in graph[start]:
        total += search(node, target)
    return total


def main():
    global graph
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [line.split(": ") for line in data]
        graph = {key: tuple(values.split(" ")) for key, values in data}
        # print(edges)
        svr_to_dac = search("svr", "dac")
        dac_to_fft = search("dac", "fft")
        fft_to_out = search("fft", "out")

        svr_to_fft = search("svr", "fft")
        fft_to_dac = search("fft", "dac")
        dac_to_out = search("dac", "out")

    total = svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out
    print(total)


if __name__ == "__main__":
    main()
