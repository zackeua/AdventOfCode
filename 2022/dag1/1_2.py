import sys

def is_num(num):
    return num != ''
        
def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [elem.strip() for elem in data]
        #print(data)
        totals = []
        maximum = 0
        temp_total = 0
        for elem in data:
            if is_num(elem):
                temp_total += int(elem)
            else:
                totals.append(temp_total)
                temp_total = 0
        totals.append(temp_total)
        m1 = max(totals)
        m2 = max([elem for elem in totals if elem != m1])
        m3 = max([elem for elem in totals if elem != m1 and elem != m2])
       
        print(m1 + m2 + m3)
if __name__ == '__main__':
    main()
