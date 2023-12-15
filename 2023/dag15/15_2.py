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
        boxes = [[] for _ in range(256)]
        for string in data:
            if '-' in string:
                label, rest = string.split('-')
                box_id = hashing(label)
                for i, elem in enumerate(boxes[box_id]):
                    if elem[0] == label:
                        boxes[box_id].pop(i)

            elif '=' in string:
                label, rest = string.split('=')
                box_id = hashing(label)
                added = False
                for i, elem in enumerate(boxes[box_id]):
                    if elem[0] == label:
                        added = True
                        boxes[box_id][i] = (label, int(rest))
                if not added:
                    boxes[box_id].append((label, int(rest)))

        focusing_power = 0
        for i, box in enumerate(boxes, start=1):
            for j, (label, focus_length) in enumerate(box, start=1):
                focusing_power += i * j * focus_length

        print(focusing_power)
    

if __name__ == '__main__':
    main()

