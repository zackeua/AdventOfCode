import sys

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [elem.strip() for elem in data]
    data = [elem[:-1].split('[') for elem in data]
    data = [[text[:text.rfind('-')], int(text[text.rfind('-')+1:]), letters] for text, letters in data]

sum_of_id = 0
letters = 'abcdefghijklmnopqrstuvwxyz'
for text, sector_id, checksum in data:
    add_to_sum = True
    letter_counts = [(text.count(letter), letter) for letter in letters]
    letter_counts.sort(key=lambda x: x[0], reverse=True)
    for index, letter in enumerate(checksum):
        if not letter == letter_counts[index][1]:
            add_to_sum = False
    if add_to_sum: sum_of_id += sector_id

print(sum_of_id)