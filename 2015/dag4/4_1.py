import hashlib


key = "bgvyzdsv"

i = 0
while True:
    result = hashlib.md5((key+str(i)).encode())
    result = result.hexdigest()
    #print(result)
    if result[:5] == '00000' and result[5] in '0123456789':
        print(i)
        break
    i += 1
