import sys

def is_num(num):
    try:
        int(num)
        return True
    except:
        return False

def main():

    count = 0
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [row.replace('\n', '') for row in data]
        dirs = {}
        parent_dirs = [''] # initial / root directory
        dirs[''] = 0
        for line in data[1:]:
            if '$ cd' in line: # Change directories
                if '..' in line: # go up one level
                    parent_dirs = parent_dirs[:-1]
                else: # go down one level
                    count += 1
                    assert(line != '$ cd ..')
                    # add new dir name after all parents to get absolute path
                    current_dir = '/'.join([parent_dirs[-1],line.split(' ')[-1]])
                    assert(current_dir not in dirs)
                    dirs[current_dir] = 0 # initialize current dir size
                    parent_dirs.append(current_dir)

            elif 'dir' in line: # just skip
                pass

            else:
                elems = line.split(' ')
                if is_num(elems[0]): # If file add that size to all parent dirs
                    for parent in parent_dirs:
                        dirs[parent] += int(elems[0])



        sorted_sizes = [dirs[d] for d in dirs]
        directories = [d for d in dirs]
        for dir in directories:
            print(dir)
        

        sorted_sizes.sort()

        print(sorted_sizes)
        print(len(sorted_sizes))
        for elem in sorted_sizes:
            if 70000000 - dirs[''] + elem >= 30000000:
                 print(elem)
                 sys.exit()
 

if __name__ == '__main__':
    main()
