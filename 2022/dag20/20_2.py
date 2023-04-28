import sys

debug = False


decryption_key  = 811589153


class Number:
    def __init__(self, original_position, value) -> None:
        self._original_position = original_position
        self._value = value
        self._current_position = original_position

    
    def copy(self):
        result = Number(self._original_position, self._value)
        result._current_position = self._current_position
        return result


def debug_print(*s, **args):
    if debug:
        print(*s, **args)

def show_array(array):
    debug_print(', '.join([str(elem._value) for elem in array]))



def shuffle(data: list[Number]):

    length = len(data)

    for index, _ in enumerate(data): # the original order of the elements

        for number in data: # get current position
            if number._original_position == index:
                i = number._current_position
        

        current_element = data[i].copy()
        assert(i == current_element._current_position)

        new_position = i + current_element._value


        if new_position < 0:
            new_position = new_position + new_position // (length - 1)
        if new_position >= length:
            new_position = new_position + new_position // (length - 1)

        #new_position = new_position + new_position // length
        new_position = new_position % length

        if new_position < i: # move everything from new_position to i up one step
            for pos in range(i, new_position, -1):
                data[pos] = data[pos - 1]
                data[pos]._current_position = pos


        elif i < new_position: # move everything from i to new_position down one step
            for pos in range(i, new_position):
                data[pos] = data[pos + 1]
                data[pos]._current_position = pos



        data[new_position] = current_element
        data[new_position]._current_position = new_position

    # move everything so 0 is at the start of the list
    while data[0]._value != 0:
        data.append(data.pop(0))

    # fix current_position
    for index, _ in enumerate(data):
        data[index]._current_position = index
            

    return data

def main():

    with open(sys.argv[1], 'r') as f:
        data = [Number(index, decryption_key * int(elem)) for index, elem in enumerate(f.readlines())]
        

        debug_print('Initial arrangement:')
        show_array(data)
        debug_print()
        for i in range(1, 10 + 1):
            data = shuffle(data)
            debug_print(f'After {i} round{"s" if i > 1 else ""} of mixing:')
            show_array(data)
            debug_print()


        index_of_0 = [elem._value for elem in data].index(0)
        for elem in data:
            if elem._value == 0:
                assert(index_of_0 == elem._current_position)

        
        print(data[(index_of_0 + 1000) % len(data)]._value)
        print(data[(index_of_0 + 2000) % len(data)]._value)
        print(data[(index_of_0 + 3000) % len(data)]._value)
        print(sum([data[(index_of_0 + i) % len(data)]._value for i in [1000, 2000, 3000]]))


if __name__ == '__main__':
    main()
