import sys
import hashlib

with open(sys.argv[1], 'r') as f:
    data = f.readline()

passkey = ''

index = 0
print(data + str(index))

while len(passkey) < 8:
    result = hashlib.md5((data+str(index)).encode())
    result = result.hexdigest()
    if result[:5] == '00000': passkey += result[5]
    #print(result)
    #print(result[:5])
    #input()
    index += 1
print(passkey)