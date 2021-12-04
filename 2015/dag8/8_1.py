import re
with open('input8.txt', 'r') as f:
        data = f.readlines()
        data = [row[:-1] for row in data]
lengths = [len(row) for row in data]
print(data)
data = [re.sub(r"\\x([0-9a-f]){2}|\\\"|\\\\", '*', row) for row in data]
print(data)
chars = [len(row)-2 for row in data]
print(lengths)
print(chars)
print(sum(lengths)-sum(chars))
