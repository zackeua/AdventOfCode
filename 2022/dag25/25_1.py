import sys

def convert_number(number_string: str) -> int:
    new_number_string =  number_string.replace('2', '4').replace('1','3').replace('0', '2').replace('-', '1').replace('=', '0')
     
    number = int(new_number_string, 5) - int('2'*len(new_number_string),5)

    return number

def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return s

def convert_back(number: int) -> str:
    temp_string = to_base_5(number)
    temp_number = int(temp_string, 5) + int('2'*len(temp_string),5)
    temp_string = to_base_5(temp_number)
    return temp_string.replace('0', '=').replace('1', '-').replace('2', '0').replace('3', '1').replace('4', '2')
    

def main():
    with open(sys.argv[1], 'r') as f:
        data = [convert_number(elem.replace('\n', '')) for elem in f.readlines()]

        print()
        #print(convert_number('2=-1=0'))
        print(convert_back(sum(data)))

if __name__ == '__main__':
    main()