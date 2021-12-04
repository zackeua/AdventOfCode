import sys
with open(sys.argv[1], 'r') as f:
    data = f.readlines()

byr = 0
iyr = 0
eyr = 0
hgt = 0
hcl = 0
ecl = 0
pid = 0
#cid = 0

count = 0


for row in data:
    if row == "\n":
        print(byr*iyr*eyr*hgt*hcl*ecl*pid==1)
        count += byr*iyr*eyr*hgt*hcl*ecl*pid==1
        byr = 0
        iyr = 0
        eyr = 0
        hgt = 0
        hcl = 0
        ecl = 0
        pid = 0
    else:
        for elem in row[:-1].split():
            if not byr and "byr" in elem:
                num = elem[4:]
                if len(num) == 4:
                    cc = 1
                    for c in num:
                         if c not in "0123456789":
                             cc = 0
                    if cc:
                        if 1920 <= int(num) <= 2002:
                            byr = 1

            if not iyr and "iyr" in elem:
                num = elem[4:]
                if len(num) == 4:
                    cc = 1
                    for c in num:
                        if c not in "0123456789":
                            cc = 0
                    if cc:
                        if 2010 <= int(num) <= 2020:
                            iyr = 1

            if not eyr and "eyr" in elem:
                num = elem[4:]
                if len(num) == 4:
                    cc = 1
                    for c in num:
                        if c not in "0123456789":
                            cc = 0
                    if cc:
                        if 2020 <= int(num) <= 2030:
                            eyr = 1

            if not hgt and "hgt" in elem:
                unit = elem[-2:]
                num = elem[4:-2]
                cc = len(num) != 0
                for c in num:
                    if c not in "0123456789":
                        cc = 0
                if cc:
                    if unit == "cm":
                        if 150 <= int(num) <= 193:
                            hgt = 1
                    if unit == "in":
                        if 59 <= int(num) <= 76:
                            hgt = 1

            if not hcl and "hcl" in elem:
                if elem[4] == "#" and len(elem[5:]) == 6:
                    cc = 1
                    for c in elem[5:]:
                        if c not in "0123456789abcdef":
                            cc = 0
                    hcl = cc
            if not ecl and "ecl" in elem:
                if elem[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    ecl = 1
            if not pid and "pid" in elem:
                if len(elem[4:]) == 9:
                    cc = 1
                    for c in elem[4:]:
                        if c not in "0123456789":
                            cc = 0
                    pid = cc
print(byr*iyr*eyr*hgt*hcl*ecl*pid==1)
count += byr*iyr*eyr*hgt*hcl*ecl*pid==1
print(count)
