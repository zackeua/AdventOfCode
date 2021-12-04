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
        #print(byr*iyr*eyr*hgt*hcl*ecl*pid==1)
        count += byr*iyr*eyr*hgt*hcl*ecl*pid==1
        byr = 0
        iyr = 0
        eyr = 0
        hgt = 0
        hcl = 0
        ecl = 0
        pid = 0
    if not byr and "byr" in row:
        byr = 1
    if not iyr and "iyr" in row:
        iyr = 1
    if not eyr and "eyr" in row:
        eyr = 1
    if not hgt and "hgt" in row:
        hgt = 1
    if not hcl and "hcl" in row:
        hcl = 1
    if not ecl and "ecl" in row:
        ecl = 1
    if not pid and "pid" in row:
        pid = 1

count += byr*iyr*eyr*hgt*hcl*ecl*pid==1

print(count)
