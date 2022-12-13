import sys
import ast
import copy

debug = False

def debug_print(*s, **args):
    if debug:
        print(*s, **args)



def is_int(elem):
    try:
        int(elem)
        return True
    except:
        return False

def is_list(elem):
    return type(elem) == type([])

 
def compare(list1, list2, indent=0):
    debug_print(f'{"  "*indent}- Compare {list1} vs {list2}')
    local_list1 = copy.deepcopy(list1)
    local_list2 = copy.deepcopy(list2)
        

    if is_int(local_list1) and is_int(local_list2):
        #print(local_list1, local_list2)
        if local_list1 == local_list2:
            return False, False
        elif  local_list1 < local_list2:
            debug_print(f'{"  "*(indent+1)}- Left side is smaller, so inputs are in the right order')
            return True, True
        else:
            debug_print(f'{"  "*(indent+1)}- Right side is smaller, so inputs are not in the right order')
            return False, True
    elif is_int(local_list1):
        local_list1 = [local_list1]
        debug_print(f'{"  "*(indent+1)}- Mixed types; convert left to {local_list1} and retry comparison  ')
        #return compare(local_list1, local_list2, indent+1)
    elif is_int(local_list2):
        local_list2 = [local_list2]
        debug_print(f'{"  "*(indent+1)}- Mixed types; convert right to {local_list2} and retry comparison  ')
        #return compare(local_list1, local_list2, indent+1)
        
    
    for i in range(max([len(local_list1), len(local_list2)])):
        try: 
            if is_int(local_list1[i]) and is_int(local_list2[i]):
                result, should_return = compare(local_list1[i], local_list2[i], indent + 1)
                if should_return:
                    return result, True
            elif is_list(local_list1[i]) and is_list(local_list2[i]):
                result, should_return = compare(local_list1[i], local_list2[i], indent + 1)
                if should_return:
                    return result, True
            elif is_int(local_list1[i]):
                result, should_return = compare([local_list1[i]], local_list2[i], indent + 1)
                if should_return:
                    return result, True
            else:
                result, should_return = compare(local_list1[i], [local_list2[i]], indent + 1)
                if should_return:
                    return result, True
        except:
            if not len(local_list1) < len(local_list2):
                debug_print(f'{"  "*(indent+1)}- Right side ran out of items, so inputs are not in the right order')
            else:
                debug_print(f'{"  "*(indent+1)}- Left side ran out of items, so inputs are in the right order')

            return len(local_list1) < len(local_list2), True
    #return True
    return len(local_list1) < len(local_list2), False

def main():

    with open(sys.argv[1], 'r') as f:
        data = [line for line in f.readlines()]
        result = 0

        assert(is_int(1))
        assert(not is_int([1,1,3]))
        assert(not is_int([1,1,[1,3]]))
        assert(is_list([1]))
        assert(is_list([[[[]]]]))
        assert(is_list([]))

        data = [ast.literal_eval(line) for line in data if line != data[2]]
        data += [[[2]]]
        data += [[[6]]]
        sorted_list = []
        result = 1
        index = 1
        while data != []:
            elem = data[0]
            data = data[1:]
            
            i = 0
            while i < len(data):
                other_elem = copy.deepcopy(data[i])
                c, _ = compare(other_elem, elem)
                if c:
                    temp_elem = other_elem
                    data[i] = copy.deepcopy(elem)
                    elem = temp_elem
                i += 1
            sorted_list.append(elem)
            if elem == [[2]] or elem == [[6]]:
                result *= index
            index += 1


        print(result)



if __name__ == '__main__':
    main()
