import sys

mapping = {'1':'1', '2':'2', '3':'3', '4':'4',
           '5':'5', '6':'6', '7':'7', '8':'8', '9':'9',
           'one':'1', 'two':'2', 'three':'3',
           'four': '4', 'five': '5','six':'6',
           'seven':'7','eight':'8','nine':'9'}

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        total = 0

        for line in data:
            print(line)
            start_pos = 100000
            start_number = ''
            end_pos = -1
            end_number = ''
            for key, val in mapping.items():
                potential_start = line.find(key)
                potential_end = line.rfind(key)
                if potential_start != -1 and  potential_start < start_pos:
                    start_pos = potential_start
                    start_number = val
                
                if potential_end != -1 and potential_end > end_pos:
                    potential_end = potential_end
                    end_number = val

            number = int(start_number + end_number)

            
            print(number)
            total += int(number)
        print(total)


if __name__ == '__main__':
    main()