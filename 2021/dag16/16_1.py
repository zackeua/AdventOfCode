import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [bin(int(row,16))[2:] for row in data]
data = data[0]

while(len(data)%4 != 0):
    data = '0' + data

def decode(packet, i=0, tot_version=0):
    version = int(packet[i:i+3],2)
    i += 3
    type_id = int(packet[i:i+3],2)
    #print(version)
    tot_version += version
    #print(type_id)
    i += 3
    if type_id == 4: # literal value
        num = ''
        parse_nums = True
        while parse_nums:
            #print(num)
            if packet[i] == '0': parse_nums = False
            num += packet[i+1:i+5]
            i += 5
        num = int(num, 2)
        #print('Literal value: ', num)
    else: # operator
        length_type_id = int(packet[i:i+1], 2)
        i += 1
        if length_type_id == 0:
            #print(packet[i:i+15])
            length = int(packet[i:i+15], 2)
            i += 15
            I = i
            #print(length)
            while i - I < length:
                i, tot_version = decode(packet, i, tot_version)
        else:
            #print(packet[i:i+11])
            number = int(packet[i:i+11], 2)
            i += 11
            n = 0
            while n < number:
                i, tot_version = decode(packet, i, tot_version)
                n += 1
            

    return i, tot_version



#print(data)
i, tot_version = decode(data, tot_version=0)

print(tot_version)