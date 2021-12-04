def binSearch(l,num):
    le = len(l)
    if le >= 2:
        if num in l[le//2:]:
            return le//2 + binSearch(l[le//2:],num)
        else:
            return binSearch(l[:le//2],num)
    else:
        return 0


nums = [9,19,1,6,0,5,4]
#nums = [0,3,6]

spoken = {}
c = len(nums)

for i,elem in enumerate(nums):
    if elem not in spoken:
        spoken[elem] = []
    spoken[elem].append(i+1)

last = nums[-1]

while c < 30000000:
    print(c)
    #print(spoken)
    #print(last)
    if len(spoken[last]) < 2:
        spoken[0].append(c+1)
        last = 0
    else:
        add = spoken[last][-1]-spoken[last][-2]
        if add not in spoken:
            spoken[add] = []
        spoken[add].append(c+1)
        last = add
    c += 1

#for key in list(spoken.keys()):
    #print(f'{key}: {spoken[key]}')

print(last)
