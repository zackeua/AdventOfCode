import re

with open('input5.txt','r') as f:
    data = f.readlines()

count = 0
s1 = ""
s2 = ""
for c1 in range(ord('a'),ord('z')+1):
    for c2 in range(ord('a'), ord('z')+1):
        s1 = s1 + "([a-z]*)" + chr(c1) + chr(c2) + "([a-z]*)" + chr(c1) + chr(c2) + "([a-z]*)" + '|'
    s2 = s2 + "([a-z]*)" + chr(c1) + "[a-z]" + chr(c1) + "([a-z]*)" + "|"

s1 = s1[:-1]
s2 = s2[:-1]

for i, row in enumerate(data):
    if None != re.match(s1,row):
        print('pass1')
        if None != re.match(s2,row):
            print('pass2')
            count += 1
print(count)



#"[a-z]*+s[a-z]*s[a-z]*, [a-z]*s[a-z]s[a-z]*"
