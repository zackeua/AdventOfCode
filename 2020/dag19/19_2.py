import re
import sys
'''
def subs(s):
    #print(s)
    d = s.split('|')
    res = ""
    for part in d:
        p = [elem for elem in part.split() if elem != ""]
        p_copy = [elem for elem in p]
        Continue = True
        for i in range(len(p)):
            if p[i].isnumeric() and Continue:
                rule = rules[p[i]]
                if '|' in rule:
                    rule1, rule2 = rule.split('|')
                    if len(p) >= maxLen/2 and p[i] in ['8', '11']:
                        p[i] = rule1
                        p_copy[i] = rule1
                    else:
                        p[i] = rule1
                        p_copy[i] = rule2
                else:
                    p[i] = rule
                    p_copy[i] = rule
                Continue = False

        if p == p_copy:
            for i in range(len(p)):
                res += p[i] + " "
            res += "| "
        else:
            for i in range(len(p)):
                res += p[i] + " "
            res += "| "
            for i in range(len(p)):
                res += p_copy[i] + " "
            res += "| "
    res = res[:-3]

    if res == s:
        return res
    else:
        return subs(res)
'''

def subs(s):
    p = [elem for elem in s.split() if elem != '']
    for i in range(len(p)):
        if p[i].isnumeric():
            p[i] = f'( {rules[p[i]]} )'
    s_new = ""
    for i in range(len(p)):
        s_new += p[i] + " "
    s_new = s_new[:-1]

    if s_new != s:
        return subs(s_new)
    else:
        return s_new


with open(sys.argv[1], 'r') as f:
    data = f.readlines()

rules = {}
t = True

for i in range(len(data)):
    data[i] = data[i][:-1]


for index, row in enumerate(data):
    if row == '':
        t = False
        begin = index
    if t:
        r = row
        r = re.sub("\"","",r)
        #print(r)
        r, rule = r.split(':')
        rules[r] = rule[1:]

#print(rules)

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

rules['8'] = '42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42 | 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42'
rules['11'] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 31 31 31'


s = rules['0']

maxLen = 0
for i in range(begin+1, len(data)):
    if len(data[i]) >= maxLen:
        maxLen = len(data[i])


#print(s)


expression = subs(s)
expression = re.sub(" ","",expression)
print(expression)



sum = 0
for i in range(begin+1,len(data)):
    print(data[i])
    data[i] = re.sub(expression,"hh",data[i])
    sum += data[i] == "hh"
print(data[begin:])
print(sum)
