import sys

def is_num(num):
    return num != ''
        
def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [elem.strip() for elem in data]
        #print(data)
        maximum = 0
        temp_total = 0
        for elem in data:
            if is_num(elem):
                temp_total += int(elem)
            else:
                if temp_total > maximum:
                    maximum = temp_total
                temp_total = 0
        if temp_total > maximum:
            maximum = temp_total
        print(maximum)
if __name__ == '__main__':
    main()
