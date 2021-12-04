import hashlib


key = "bgvyzdsv"

i = 0
while True:
    result = hashlib.md5((key+str(i)).encode())
    result = result.hexdigest()
    #print(result)
    if result[:6] == '00000':
        print(i)
        break
    i += 1
