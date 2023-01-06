import sys

debug = False

def debug_print(*s, **args):
    if debug:
        print(*s, **args)

def show_array(array):
    debug_print(', '.join([str(elem[0]) for elem in array]))

def main():

    with open(sys.argv[1], 'r') as f:
        data = [(int(elem), False) for elem in f.readlines()]

        i = 0
        length = len(data)
        debug_print('Initial arrangement:')
        show_array(data)
        debug_print()
        while i < len(data):
            current_element = data[i]
            if current_element[1]:
               i += 1
            else:
                position = i + current_element[0]

                debug_print(position)
                if position < 0:
                    position = position + position // length
                if position > length:
                    position = position + position // length

                position = position % length

                if position < i:
                    for pos in range(i, position, -1):
                        data[pos] = data[pos - 1]
                elif i < position:
                    for pos in range(i, position):
                        data[pos] = data[pos + 1]

                data[position] = (current_element[0], True)
            

                if i == position:
                    debug_print(f'{current_element[0]} does not move:')
                else:
                    debug_print(f'{current_element[0]} moves between {data[(position - 1) % length][0]} and {data[(position + 1) % length][0]}:')
                show_array(data)
                #debug_print(data)
                debug_print()
        
        print([elem for elem in data])
        assert(all([elem[1] for elem in data]))
        numbers = [elem[0] for elem in data]
        index_of_0 = numbers.index(0)
        print(numbers[(index_of_0+1000)%len(numbers)])
        print(numbers[(index_of_0+2000)%len(numbers)])
        print(numbers[(index_of_0+3000)%len(numbers)])
        assert(len(numbers) == length)
        print(sum([numbers[(index_of_0+i)%len(numbers)] for i in [1000, 2000, 3000]]))
if __name__ == '__main__':
    main()