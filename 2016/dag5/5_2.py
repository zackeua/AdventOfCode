import sys
import hashlib

with open(sys.argv[1], 'r') as f:
    data = f.readline()

passkey = [None]*8

index = 0
print(data + str(index))

while None in passkey:
    result = hashlib.md5((data+str(index)).encode())
    result = result.hexdigest()
    if result[:5] == '00000':
        if result[5] in '01234567':
            if passkey[int(result[5])] == None: passkey[int(result[5])] = result[6]
    index += 1
print(''.join(passkey))