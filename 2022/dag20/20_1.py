import sys

def show_array(array):
    print(', '.join([str(elem[0]) for elem in array]))

def main():

    with open(sys.argv[1], 'r') as f:
        data = [(int(elem), False) for elem in f.readlines()]

        i = 0
        length = len(data)
        print('Initial arrangement:')
        show_array(data)
        input()
        while i < len(data):
            current_element = data[i]
            if current_element[1]:
               i += 1
            else:
                data.pop(i)
                position = i + current_element[0]
                if position < i:
                    position -= 1
                while position > length:
                    position -= length
                while position < 0:
                    position += length
                if i == position:
                    print(f'{current_element[0]} does not move:')
                else:
                    print(f'{current_element[0]} moves between {data[(position-1)%(length-1)][0]} and {data[position%(length-1)][0]}:')
                data.insert(position,  (current_element[0], True))
                show_array(data)
                input()
            


        print([elem[0] for elem in data])


if __name__ == '__main__':
    main()