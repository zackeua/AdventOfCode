with open('input9.txt','r') as f:
    data = f.readlines()
    data = list(map(int,data))

for i in range(25,len(data)):
    dat = data[i-25:i]
    ok = 0
    for j in range(len(dat)):
        for k in range(len(dat)):
            if j != k and dat[j] + dat[k] == data[i]:
                ok = (j,k)
    if ok == 0:
        print(data[i])
        nosum = data[i]
        break

for i in range(len(data)):
    beginIndex = i
    index = i
    tot = 0
    while tot < nosum:
        tot += data[index]
        index += 1
    if totsum == nosum:
        endIndex = index
        break
nums = data[beginIndex:endIndex]
nums.sort()
print(nums[0]+nums[-1])
