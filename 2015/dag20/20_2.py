import sys
import numpy as np

with open(sys.argv[1], 'r') as f:
    input_val = int(f.readline())

n = 0
find = False

presents = np.zeros(shape=(max([input_val//10+1, 100]),))

for elf in range(1, len(presents)+1):
    for house in range(elf-1, min([50*elf, len(presents)]), elf):
        presents[house] += elf*11


print(np.argwhere(presents > input_val)[0]+1)
