import sys

debug = True

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
                was_greater = False
                was_less = False
                while position <= 0:
                    position += length-1
                
                while position > length:
                    was_greater = True
                    position -= length-1

                if was_greater:
                    position -= 1
                
                if was_less:
                    position += 1

                data.insert(position+1,  (current_element[0], True))
                
                offset = 0
                if i < position:
                    data.pop(i)
                elif i == position:
                    data.pop(i)
                else:
                    offset = 1
                    data.pop(i+1)
                
                if i == position:
                    debug_print(f'{current_element[0]} does not move:')
                    i += 1
                else:
                    pass
                    debug_print(f'{current_element[0]} moves between {data[(position-1+offset)%length][0]} and {data[(position+1+offset)%length][0]}:')
                #print(i, position+1)
                show_array(data)
                debug_print()
            

        #print(data)

        print([elem[0] for elem in data])
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