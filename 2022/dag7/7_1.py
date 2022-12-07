import sys

def is_num(num):
    try:
        int(num)
        return True
    except:
        return False

def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [row.replace('\n', '') for row in data]
        dirs = {}
        current_dir = '/'
        previous_dir = []
        previous_child_dirs = []
        child_dirs = []
        total = 0
        previous_total = []
        print('- / (dir)')
        for i, line in enumerate(data[1:]):
            if 'cd' in line:
                if '..' not in line: # go down one level
                    previous_dir.append(current_dir)
                    current_dir = previous_dir[-1] + '/' + line.split(' ')[-1]
                    previous_child_dirs.append(child_dirs.copy())
                    child_dirs = []
                    previous_total.append(total)
                    total = 0
                else: # go up one level
                    dirs[current_dir] = total + sum([dirs[dir] for dir in child_dirs if dir in dirs])
                    current_dir = previous_dir[-1]
                    previous_dir = previous_dir[:-1]
                    child_dirs = previous_child_dirs[-1]
                    previous_child_dirs = previous_child_dirs[:-1]
                    total = previous_total[-1]
                    previous_total = previous_total[:-1]

            elif 'dir' in line:
                path = current_dir + '/' + line.split(' ')[1]
                print(path)
                child_dirs.append(path)
                taps = "  "*(len(previous_dir)+1)
                print(f'{taps}- {child_dirs[-1]} (dir)')
            else:
                elems = line.split(' ')
                if len(elems) == 2:
                    if is_num(elems[0]):
                        total += int(elems[0])
                        taps = "  "*(len(previous_dir)+1)
                        print(
                            f'{taps}- {elems[1]} (file, size={int(elems[0])})')

        while previous_dir != []:
            path = current_dir
            dirs[path] = total + sum([dirs[dir] for dir in child_dirs if dir in dirs])
            current_dir = previous_dir[-1]
            previous_dir = previous_dir[:-1]
            child_dirs = previous_child_dirs[-1]
            previous_child_dirs = previous_child_dirs[:-1]
            total = previous_total[-1]
            previous_total = previous_total[:-1]

        
        total = 0
        for dir in [d for d in dirs]:
            if dirs[dir] <= 100000:
                total += dirs[dir] 
        print(total)

                

        
        #data = [row.split('\n') for row in data]
 

if __name__ == '__main__':
    main()
