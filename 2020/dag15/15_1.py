def binSearch(l,num):
    le = len(l)
    if le >= 2:
        if num in l[le//2:]:
            return le//2 + binSearch(l[le//2:],num)
        else:
            return le//2 - binSearch(l[:le//2],num)
    else:
        return 0


spoken = [9,19,1,6,0,5,4]
#spoken = [0,3,6]
c = len(spoken)


while c < 2020:
    print(c)
    num = spoken[-1]
    if num not in spoken[:-1]:
        spoken.append(0)
    else:
        i = c-2
        while spoken[i] != num:
            i -= 1
        spoken.append(c-i-1)
    c += 1

print(spoken[-1])
