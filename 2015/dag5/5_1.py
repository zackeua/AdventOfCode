import re

with open('input5.txt','r') as f:
    data = f.readlines()

count = 0
s = ""
for c in range(ord('a'),ord('z')+1):
    s = s + chr(c) + chr(c) + '|'
s  = f'([a-zA-Z]*)({s[:-1]})([a-zA-Z]*)'
print(s[:-1])
for i, row in enumerate(data):
    print(f'row: {i}, {row[:-1]}:')
    if None != re.match("([a-zA-Z]*)[aeiou]([a-zA-Z]*)[aeiou]([a-zA-Z]*)[aeiou]([a-zA-Z]*)",row):
        print('pass1')
        if None != re.match(s,row):
            print('pass2')
            if None == re.match("([a-zA-Z]*)(ab|cd|pq|xy)([a-zA-Z]*)",row):
                print('pass3')
                count += 1
print(count)
