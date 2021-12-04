import re
with open('input8.txt', 'r') as f:
    data = f.readlines()
    data = [row[:-1] for row in data]
lengths = [len(row) for row in data]
print(data)
data = [re.sub(r"\\|\"", '**', row) for row in data]
print(data)
chars = [len(row)+2 for row in data]
print(lengths)
print(chars)
print(sum(chars)-sum(lengths))
