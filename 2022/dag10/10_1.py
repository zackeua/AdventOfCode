import sys

def if_in_cycle(cycle, register, result):
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength = cycle * register['X']
        #print(signal_strength)
        #print(register['X'])
        return result + signal_strength
    return result

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [line.replace('\n', '') for line in data]
        register = {'X': 1}
        result = 0
        cycle = 0
        for _, line in enumerate(data):

            #print(cycle, register, result, line)
            if 'addx' in line:
                _, amount = line.split()
                cycle += 1
                result = if_in_cycle(cycle, register, result)
                cycle += 1
                result = if_in_cycle(cycle, register, result)
                register['X'] += int(amount)

            else:
                cycle += 1
                result = if_in_cycle(cycle, register, result)

        
            
        print(result)

if __name__ == '__main__':
    main()
